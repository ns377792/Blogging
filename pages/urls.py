from django.urls import path
from . import views
urlpatterns = [
    path('<str:page>', views.page, name="Page")
]
