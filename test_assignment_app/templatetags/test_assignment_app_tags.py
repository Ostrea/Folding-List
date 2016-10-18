from django import template

from ..models import Menu


register = template.Library()


@register.inclusion_tag('test_assignment_app/menu.html')
def draw_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    return {'items': nested_to_flat(menu, True)}


def nested_to_flat(node, highest_level_menu):
    if node.children.exists():
        yield {'link': node.link, 'data': node.name, 'is_data': True}
        yield {'start_nodes': True, 'highest_level_menu': highest_level_menu,
               'menu_name': node.name.lower().replace(' ', '_')}

        for menu_item in node.children.all():
            yield {'start_node': True}
            for item in nested_to_flat(menu_item, False):
                yield item
            yield {'end_node': True}

        yield {'end_nodes': True}
    else:
        yield {'link': node.link, 'data': node.name, 'is_data': True}
