from django.contrib import admin
from .models import Category, Comment, Contact, blogpost
# Register your models here.


class blogPostAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description', 'slug', 'content']
    list_display = ['name', 'category', 'description', 'slug', 'date']
    class Media:
        js= ('blog/tinyInject.js',)
        
class commentAdmin(admin.ModelAdmin):
    list_display = ['user', 'blog_post','comment', 'date']

class contactAdmin(admin.ModelAdmin):
    list_display = ['sno','name','phone','email','timeStamp']


admin.site.register(blogpost, blogPostAdmin)
admin.site.register(Category)
admin.site.register(Contact, contactAdmin)
admin.site.register(Comment, commentAdmin)