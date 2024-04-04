from django import template
from django.conf import settings
from ..models import Menu

register = template.Library()


def get_menu_item_by_title(all_menu: list, title: str) -> dict:
    menu_item = {}
    for item in all_menu:
        if item['title'] == title:
            menu_item = item
            break
    return menu_item


def get_menu_items_by_head_menu(all_menu: list, head_menu: str) -> list:
    menu_items = []
    for item in all_menu:
        if item['head_menu'] == head_menu:
            menu_items.append(item)
    return menu_items


@register.inclusion_tag('core/tag_menu.html', takes_context=True)
def draw_menu(context, menu_title):
    request_title = ''
    temp_menu = []
    error = ''

    if settings.MENU_URL_PREFIX in context.request.path:
        request_title = context.request.path[1:-1].split('/')[::-1][0]

    menu_title = request_title.replace('_', ' ') if request_title else menu_title

    queryset_all_menu = Menu.objects.select_related('head_menu')

    all_menu = [
        {
            'title': item.title,
            'head_menu': item.head_menu.title if item.head_menu else '',
            'menu_url': item.menu_url
        } for item in queryset_all_menu
    ]

    my_menu = get_menu_item_by_title(all_menu, menu_title)
    if not my_menu:
        error = 'This menu does not exist!'
        return {'error': error}

    sub_menu = get_menu_items_by_head_menu(all_menu, my_menu['title'])
    if sub_menu:
        for item in sub_menu:
            temp_menu.append({
                'title': item['title'],
                'url': item['menu_url'],
                'children': []
            })

    result_menu = get_full_menu(all_menu, current_menu=my_menu, temp_menu=temp_menu)

    return {'menu': result_menu, 'menu_title': menu_title, 'error': error}


def get_full_menu(all_menu, current_menu, temp_menu):
    while current_menu['head_menu']:
        menu = [{
            'title': current_menu['title'],
            'url': current_menu['menu_url'],
            'children': []
        }]

        if temp_menu:
            for item in temp_menu:
                menu[0]['children'].append(item)

        menu_at_the_same_levels = get_menu_items_by_head_menu(all_menu, head_menu=current_menu['head_menu'])

        if menu_at_the_same_levels:
            for menu_item in menu_at_the_same_levels:

                temp_title = [item['title'] for item in menu]

                if menu_item['title'] not in temp_title:
                    menu.append(
                        {
                            'title': menu_item['title'],
                            'url': menu_item['menu_url'],
                        }
                    )

        temp_menu = menu
        current_menu = get_menu_item_by_title(all_menu, title=current_menu['head_menu'])

    result_menu = [{
        'title': current_menu['title'],
        'url': current_menu['menu_url'],
        'children': None
    }]

    result_menu[0]['children'] = temp_menu

    return result_menu
