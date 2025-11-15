from django import template
from mainmenu.models import Menu
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def draw_menu(name):
    menu_items = Menu.objects.filter(name=name).select_related('category')
    return  mark_safe(render_menu(menu_items))


def render_menu(menu_items):
    menu_html = '<ul>'
    for item in menu_items:
        menu_html += '<li>'
        if item.url:
            menu_html += f'<a href="{item.url}">{item.name}</a>'
        elif item.named_url:
            menu_html += f'<a href="{item.named_url}">{item.name}</a>'
        else:
            menu_html += item.name

        if item.child.exists():
            menu_html += render_menu(item.child.all())
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html