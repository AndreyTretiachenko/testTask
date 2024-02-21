from django.contrib import admin
from .models import TreeMenu


class AdminTreeMenu(admin.ModelAdmin):
    model = TreeMenu
    list_display = ('pk', 'menu_name', 'id_parent', 'menu_url')


admin.site.register(TreeMenu, AdminTreeMenu)
