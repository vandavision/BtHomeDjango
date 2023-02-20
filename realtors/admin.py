from django.contrib import admin
from . models import Realtor
# Register your models here.
@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "is_mvp")