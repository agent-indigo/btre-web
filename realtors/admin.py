from django.contrib import admin

# Register your models here.
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first', 'last', 'email', 'hire_date')
    list_display_links = ('id', 'first', 'last')
    search_fields = ('first', 'last')
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
