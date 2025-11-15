from django.urls import path

from .views import draw_menu


urlpatterns = [
    path('<str:menu_name>/', draw_menu, name='draw_menu'),
]
