from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib import admin


# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
