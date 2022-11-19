import numpy as np
from PIL import Image
from django.shortcuts import render

# Create your views here.
from keras.saving.model_config import model_from_json
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from VAYU.settings import MEDIA_ROOT
from .abg_auto_model import abg_auto_disorder_predict
from .doctor_script import generate_report
from VAYU_MAIN.models import User
from copd.models import AbgTest, XrayTest, AbgAutoTest
from copd.serializers import AbgTestReqSerializer, AbgTestReportSerializer, XrayTestSerializer, \
    AbgAutoTestReqSerializer, AbgAutoTestReportSerializer
import os
import cv2

from .xray import test_xray

modulepath = os.path.dirname(__file__)
xrayModelJsonPath = os.path.join(modulepath, 'mlmodels/model_4.json')
xrayModelH5Path = os.path.join(modulepath, 'mlmodels/model_4.h5')
xrayMedia = MEDIA_ROOT


def convert_from_image_to_cv2(img: Image) -> np.ndarray:
    # return cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    return np.asarray(img)


class XrayTestViewSet(ViewSet):
    queryset = XrayTest.objects.all()
    serializer_class = XrayTestSerializer

    # noinspection PyMethodMayBeStatic
    def create(self, request, *args, **kwargs):
        try:
            img = request.data['xray']
            xray = XrayTest.objects.create(image=img, user=User.objects.get(id=request.data['user']), report="Rep")

            result = test_xray(os.path.join(MEDIA_ROOT, str(xray.image)))
            if result < 1:
                return Response({'result': 'Less chances of having a respiratory problem'}, status=200)
            else:
                return Response({'result': 'Chances of having a respiratory problem'}, status=200)
        except:
            return Response({'error': "Errors"})


class AbgTestViewSet(ViewSet):
    queryset = AbgTest.objects.all()

    # noinspection PyMethodMayBeStatic
    def create(self, request):

        try:
            serializer = AbgTestReqSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            abg = AbgTest()
            abg.user = User.objects.get(id=int(serializer.data["user"]))
            abg.ph = serializer.data["ph"]
            abg.paco2 = serializer.data["paco2"]
            abg.pao2 = serializer.data["pao2"]
            abg.o2sat = serializer.data["o2sat"]
            abg.hco3 = serializer.data["hco3"]
            abg.cl = serializer.data["cl"]
            abg.na = serializer.data["na"]
            abg.save()
            abg.report = generate_report(abg)
            return Response(AbgTestReportSerializer(abg).data)
        except:
            return Response({"Error": "Data Integrity Error"})

    # noinspection PyMethodMayBeStatic
    def list(self, request):
        queryset = AbgTest.objects.filter(user=request.GET.get("user"))
        print(queryset)
        for t in queryset:
            t.report = generate_report(t)
        serializer = AbgTestReportSerializer(queryset, many=True)

        return Response(serializer.data)


class AbgAutoTestViewSet(ViewSet):
    queryset = AbgAutoTest.objects.all()

    # noinspection PyMethodMayBeStatic
    def create(self, request):

        try:
            serializer = AbgAutoTestReqSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            repdata = {0: 'Metabolic Acidosis', 1: 'Metabolic Acidosis with Respiratory Acidosis',
                       2: 'Metabolic Alkalosis',
                       3: 'Normal', 4: 'Respiratory Acidosis', 5: 'Respiratory Alkalosis'}
            abg = AbgAutoTest()
            abg.user = User.objects.get(id=int(serializer.data["user"]))
            abg.ph = serializer.data["ph"]
            abg.paco2 = serializer.data["paco2"]
            abg.pao2 = serializer.data["pao2"]
            abg.o2sat = serializer.data["o2sat"]
            abg.hco3 = serializer.data["hco3"]
            abg.disorder = str(repdata[abg_auto_disorder_predict(abg)[0]])
            abg.save()
            AbgAutoTestReportSerializer(abg).data["report"] = generate_report(abg)
            return Response(AbgAutoTestReportSerializer(abg).data)
        except:
            return Response({"Error": "Data Integrity Error"})

    # noinspection PyMethodMayBeStatic
    def list(self, request):
        queryset = AbgAutoTest.objects.filter(user=request.GET.get("user"))
        print(queryset)
        for t in queryset:
            t.report = generate_report(t)
        serializer = AbgAutoTestReportSerializer(queryset, many=True)

        return Response(serializer.data)

