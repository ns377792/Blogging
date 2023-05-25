from django.contrib import admin

from pages.models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    class Media:
        js= ('blog/tinyInject.js',)
        

admin.site.register(Page, PageAdmin)