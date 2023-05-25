from django.contrib import admin

from blogtheme.models import FooterHeading, FooterLink, Nav_menu, Nav_social_media_icon, Navlog, copyrightClaim

# Register your models here.

class copyrightClaimAdmin(admin.ModelAdmin):
     list_display = ['msg','location']

class NavlogaimAdmin(admin.ModelAdmin):
     list_display = ['name', 'name2','logo']

class Nav_social_media_iconAdmin(admin.ModelAdmin):
     list_display = ['icon', 'iconlink','your_icon']

class Nav_menuAdmin(admin.ModelAdmin):
     list_display = ['your_menu', 'menuname','menuurl']

class FooterLinkAdmin(admin.ModelAdmin):
     list_display = ['head', 'name','link']

class FooterHeadingAdmin(admin.ModelAdmin):
     list_display = ['sno', 'name']

admin.site.register(Navlog,NavlogaimAdmin)
admin.site.register(Nav_menu,Nav_menuAdmin)
admin.site.register(Nav_social_media_icon,Nav_social_media_iconAdmin)
admin.site.register(FooterLink,FooterLinkAdmin)
admin.site.register(FooterHeading,FooterHeadingAdmin)
admin.site.register(copyrightClaim, copyrightClaimAdmin)