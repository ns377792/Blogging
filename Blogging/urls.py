from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.site.site_header="NITIN SINGH"
admin.site.site_title="Blogging"
admin.site.index_title="Welcome To Our Blog"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admins/', include('url.urls')),
    path('page/', include('pages.urls')),
    path('', include('blog.urls')),
    path('url/<str:query>/', views.urlshort, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
