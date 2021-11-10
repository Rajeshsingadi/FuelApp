from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# Register your models here.
from . models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display=['email','username']
    list_per_page = 20
    list_filter =['email','username']
admin.site.register(Users, UsersAdmin)