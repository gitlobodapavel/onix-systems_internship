from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.CharField()
    last_login = serializers.CharField()