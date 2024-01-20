from django.contrib import admin
from django.urls import path
from calendario.views import (
    show_cal,
    add_compromisso,
    compromisso_detail,
    compromisso_delete,
    compromisso_edit,
    search_compromissos,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", show_cal, name="show_cal"),
    path("add/", add_compromisso, name="add_compromisso"),
    path("compromisso/<int:pk>/", compromisso_detail, name="compromisso_detail"),
    path("compromisso/<int:pk>/edit/", compromisso_edit, name="compromisso_edit"),
    path("compromisso/<int:pk>/delete/", compromisso_delete, name="compromisso_delete"),
    path("search/", search_compromissos, name="search_compromissos"),
]
