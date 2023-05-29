
from email.policy import default
from django.db import models

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
# from django.contrib.gis.db import models
# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(null=False,unique=True)
    phone_number = models.CharField(max_length=10, null=False)
    password = models.CharField(
        validators=[MinLengthValidator(4)], max_length=20, null=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}"


class Registration(models.Model):
    serial_no = models.IntegerField(primary_key=True)
    user = models.ForeignKey(
        Users, null=True, blank=True, on_delete=models.PROTECT)
    registered_at = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.user_id)


class SubscriptionPlan(models.Model):
    plan_name = models.CharField(max_length=50)
    duration_month = models.IntegerField(blank=True,null=True)
    number_of_devices = models.IntegerField()
    automation_access = models.BooleanField()
    sharable_to = models.IntegerField(default = 1)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)

    def __str__(self):
        return self.plan_name
    

    def __str__(self):
        return self.plan_name


class Subscriptions(models.Model):
    subscription_plan_id = models.ForeignKey(
        SubscriptionPlan, null=True, on_delete=models.SET_NULL)
    serial_no = models.OneToOneField(
        Registration, on_delete=models.RESTRICT)
    is_active = models.BooleanField()
    purchase_date = models.DateField(auto_now_add=True, editable=False)
    expiry_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.serial_no}"


class Home(models.Model):
    serial_no = models.ForeignKey(Registration, on_delete=models.CASCADE,related_name = 'homeuser')
    name = models.CharField(max_length=50)
    latitude = models.FloatField(validators=[MinValueValidator(-90.0),
                                             MaxValueValidator(90.0)])
    longitude = models.FloatField(validators=[MinValueValidator(-180.0),
                                              MaxValueValidator(180.0)])

    def __str__(self):
        return self.name


class Area(models.Model):
    home_id = models.ForeignKey(Home, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=50)

    def __str__(self):
        return self.area_name


class Devices(models.Model):
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=50)
    is_active = models.BooleanField()
    parameters = models.TextField(
        default={"active": "off", "color": "white", "speed": None})
    
    def __str__(self):
        return self.device_name
    


class Permission(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    access_area_id = models.ManyToManyField(
        Area, verbose_name=("Select Areas"))
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name
