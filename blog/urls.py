from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('blogs/comment', views.postComment, name="postComment"),
    path('blog/<str:slug>', views.blogpostreadmore, name="blogpostreadmore"),
    path('contactus/', views.Contactus, name="contactus"),
    path('blog/category/<str:category>', views.categoryposts, name="categoryposts")
]