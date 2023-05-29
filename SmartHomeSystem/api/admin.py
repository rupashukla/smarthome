from django.contrib import admin
from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','phone_number','is_active','created_at','updated_at']

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name']
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['serial_no', 'user_id','registered_at']
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ['plan_name', 'price','duration_month','number_of_devices','automation_access','sharable_to']
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ['serial_no','subscription_plan_id','is_active','purchase_date','expiry_date']
class HomeAdmin(admin.ModelAdmin):
    list_display = ['name', 'latitude','longitude','serial_no']
class AreaAdmin(admin.ModelAdmin):
    list_display = ['home_id', 'area_name']
class DevicesAdmin(admin.ModelAdmin):
    list_display = ['area_id', 'device_name','is_active','parameters']


admin.site.register(Users, UserAdmin)
admin.site.register(Registration,RegistrationAdmin)
admin.site.register(SubscriptionPlan,SubscriptionPlanAdmin)
admin.site.register(Subscriptions,SubscriptionsAdmin)
admin.site.register(Home,HomeAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Devices,DevicesAdmin)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','user_id','role_id','created_at','updated_at','is_active']