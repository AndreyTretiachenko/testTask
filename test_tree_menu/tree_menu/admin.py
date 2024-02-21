from django.contrib import admin
from .models import TreeMenu, Menu


class AdminTreeMenu(admin.ModelAdmin):
    model = TreeMenu
    list_display = ('pk', 'menu', 'title', 'parent', 'menu_url')


class AdminMenu(admin.ModelAdmin):
    model = Menu
    list_display = ('pk', 'title', 'description')


admin.site.register(TreeMenu, AdminTreeMenu)
admin.site.register(Menu, AdminMenu)
