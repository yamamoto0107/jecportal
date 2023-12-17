from django.contrib import admin
from .models import Attend
from django.contrib.auth import get_user_model
# Register your models here.
#CustomUser = get_user_model()
admin.site.register(Attend)
#admin.site.register(CustomUser)