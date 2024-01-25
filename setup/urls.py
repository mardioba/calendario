# setup/urls.py
# /home/mardio/Projetos/calendario/setup/urls.py
# Setup é o projeto(onde ta o settings.py) e calendario o app
from django.contrib import admin
from django.urls import path, include
from calendario.views import (
    show_cal,
    add_compromisso,
    compromisso_detail,
    compromisso_delete,
    compromisso_edit,
    search_compromissos,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", show_cal, name="show_cal"),
    path("add/", add_compromisso, name="add_compromisso"),
    path("compromisso/<int:pk>/", compromisso_detail, name="compromisso_detail"),
    path("compromisso/<int:pk>/edit/", compromisso_edit, name="compromisso_edit"),
    path("compromisso/<int:pk>/delete/", compromisso_delete, name="compromisso_delete"),
    path("search/", search_compromissos, name="search_compromissos"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="custom_login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
]
