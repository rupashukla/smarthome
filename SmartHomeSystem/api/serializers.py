
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username','email','phone_number','is_active']

class RegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Registration
        fields = ['serial_no','user']
        






class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ["id"]


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ["id"]


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ["id"]


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ["id"]


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ["id"]
