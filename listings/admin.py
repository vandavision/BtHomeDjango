from django.contrib import admin
from . models import Listing
# Register your models here.
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "is_published", "list_date")