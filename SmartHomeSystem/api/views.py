from datetime import datetime, date
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def registration(request):
    if request.method == 'GET':
        users = Users.objects.all()
        # control_system_registration = ControlSystemRegistration.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)

    if request.method == 'POST':
        exist_user = Users.objects.filter(email=request.data["email"]).exists()
        if "serial_no" in request.data.keys():
            register = Registration.objects.filter(
                serial_no=request.data["serial_no"]).get()
            print(register.user_id)
            if not exist_user and register.user_id is None:
                serializer = UserSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                user = Users.objects.get(email=request.data["email"])
                user.is_active = True
                user.save()
                Registration.objects.filter(pk=request.data['serial_no']).update(
                    user_id=user.id, registered_at=str(datetime.now()))
                return Response({"message": "registered successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "already exist with this device"}, status=status.HTTP_409_CONFLICT)
        else:
            if not exist_user:
                serializer = UserSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

            else:
                return Response({"message": "already exist"}, status=status.HTTP_409_CONFLICT)

@api_view(['GET'])
def dashboard(request):
    if request.method == 'GET':
        users = Registration.objects.select_related('user').all()
        # control_system_registration = ControlSystemRegistration.objects.all()
        user_serializer = RegistrationSerializer(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)