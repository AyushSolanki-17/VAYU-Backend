from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from VAYU_MAIN.models import User
from VAYU_MAIN.serializer import SignInSerializer, SignUpSerializer


class SignInViewSet(ViewSet):
    queryset = User.objects.all()

    # noinspection PyMethodMayBeStatic
    def create(self, request):
        try:
            serializer = SignInSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            email = serializer.data["email"]
            password = serializer.data["password"]
            user = User.objects.get(email=email)
            if user.check_password(password):
                data = {"id": user.id, "email": user.email, "fullname": user.fullname}
                return Response(data)
            else:
                return Response({"Error": "Wrong Password"})
        except:
            return Response({"Error": "Data Integrity Error"})


class SignUpViewSet(ViewSet):
    queryset = User.objects.all()

    # noinspection PyMethodMayBeStatic
    def create(self, request):
        try:
            serializer = SignUpSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            email = serializer.data["email"]
            fullname = serializer.data["fullname"]
            password = serializer.data["password"]
            user = User.objects.create_user(email=email, fullname=fullname, password=password)
            user.set_password(password)
            user.save()
            data = {"id": user.id, "email": user.email, "fullname": user.fullname}
            return Response(data)
        except:
            return Response({"Error": "Data Integrity Error"})
