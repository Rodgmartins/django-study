from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("login/", views.user_authenticate, name="login"),
    path("logout/", views.user_logout, name="logout"),
]