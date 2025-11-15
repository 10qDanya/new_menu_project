from django.shortcuts import render
from .models import Menu

def draw_menu(request, name):
    menu_items = Menu.objects.filter(name=name).select_related('category')
    return render(request, ' menu.html', {'menu_items': menu_items})
