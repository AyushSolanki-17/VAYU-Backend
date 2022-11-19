from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from copd.models import AbgTest, XrayTest, AbgAutoTest


class AbgTestReqSerializer(ModelSerializer):
    class Meta:
        model = AbgTest
        fields = ["user", "ph", "paco2", "pao2", "hco3", "o2sat", "na", "cl"]


class AbgTestReportSerializer(ModelSerializer):
    report = serializers.CharField(max_length=1000)

    class Meta:
        model = AbgTest
        fields = "__all__"


class XrayTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = XrayTest
        fields = "__all__"


class AbgAutoTestReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbgAutoTest
        exclude = ["disorder"]


class AbgAutoTestReportSerializer(ModelSerializer):
    report = serializers.CharField(max_length=1000)

    class Meta:
        model = AbgAutoTest
        fields = "__all__"
