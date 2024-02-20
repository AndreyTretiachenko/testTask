from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from .models import TreeMenu


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def menu_view(request, menu_name):
    # try:
        menu_db = TreeMenu.objects.filter(menu_url=menu_name).first()
        context = {
            'menu_list': menu_db
        }
        return render(request, "tree_menu/base.html", context)
    # except:
    #     raise Http404("не найден пункт меню")
