from django.contrib import admin

# Register your models here.
from .models import Routine, User

admin.site.register(Routine)
admin.site.register(User)