from django.urls import path
from .views import dashboard, generate, home, users

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('generate/', generate, name="generate"),
    path('users/', users, name="users"),
]
