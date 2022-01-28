from django.contrib import admin

# Register your models here.

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import NonOrdinaryUser
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = NonOrdinaryUser
    list_display = ['username']

admin.site.register(NonOrdinaryUser, CustomUserAdmin)