from django.contrib import admin

# Register your models here.
from phonestore.models import *


@admin.register(Ad, User, Review, Category)
class ObjectsAdmin(admin.ModelAdmin):
    pass
