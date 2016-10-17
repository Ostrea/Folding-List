from django import template

from ..models import Menu, MenuItem


register = template.Library()


@register.inclusion_tag('test_assignment_app/menu.html')
def draw_menu(menu_name):
    menu = Menu('Super menu', [MenuItem('First'), MenuItem('Second'),
                               Menu('Third',
                                    [MenuItem('Sub third one'),
                                     Menu('Sub third two',
                                          [MenuItem('Sub sub third two')])])])
    return {'items': nested_to_flat(menu)}


def nested_to_flat(menu):
    if isinstance(menu, Menu):
        yield {'data': menu.name, 'is_data': True}
        yield {'start_nodes': True}
        for node in menu.items:
            yield {'start_node': True}
            for i in nested_to_flat(node):
                yield i
            yield {'end_node': True}
        yield {'end_nodes': True}
    else:
        yield {'data': menu.value, 'is_data': True}
