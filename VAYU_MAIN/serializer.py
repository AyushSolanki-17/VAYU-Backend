from rest_framework import serializers

from VAYU_MAIN.models import User


class SignUpSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = User
        fields = ["email", "fullname", "password"]


class SignInSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)

