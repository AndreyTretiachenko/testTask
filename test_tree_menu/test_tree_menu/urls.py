from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("menu/", include("tree_menu.urls")),
    path("admin/", admin.site.urls),
]
