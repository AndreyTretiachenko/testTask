from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from .models import TreeMenu


def index(request, menu_name=""):
    # try:
        print(menu_name)
        menu_db = TreeMenu.objects.all()
        menu_active = TreeMenu.objects.filter(menu_url = menu_name).first()
        context = {
            'menu_list': menu_db,
            'item_menu': menu_active
        }
        return render(request, "tree_menu/base.html", context)
    # except:
    #     raise Http404("нет меню")

