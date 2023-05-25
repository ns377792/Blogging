from django.contrib import admin
from .models import shorturl
# Register your models here.

class shorurladmin(admin.ModelAdmin):
    list_display = ['short_query','visits', 'date']
    search_fields = ['short_query','visits', 'date']

admin.site.register(shorturl, shorurladmin)