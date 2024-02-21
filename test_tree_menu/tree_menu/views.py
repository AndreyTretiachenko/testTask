from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from .models import TreeMenu, Menu


def index(request, menu_name: str = None):
        menu = TreeMenu.objects.filter(menu_url=menu_name).first()
        context = {

        }
        return render(request, "tree_menu/base.html", context)

