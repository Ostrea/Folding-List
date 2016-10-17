from django import template

from ..models import Menu, MenuItem


register = template.Library()


@register.inclusion_tag('test_assignment_app/menu.html')
def draw_menu(menu_name):
    menu = Menu('Super menu', 'super_menu_link',
                [MenuItem('First', 'first_link'),
                 MenuItem('Second', 'second_link'),
                 Menu('Third', 'third_link',
                      [MenuItem('Sub third one', 'sub_third_one_link'),
                       Menu('Sub third two', 'sub_third_two_link',
                            [MenuItem('Sub sub third two',
                                      'sub_sub_third_two_link')])])])

    return {'items': nested_to_flat(menu)}


def nested_to_flat(node):
    if isinstance(node, Menu):
        yield {'link': node.link, 'data': node.name, 'is_data': True}
        yield {'start_nodes': True}

        for menu_item in node.items:
            yield {'start_node': True}
            for item in nested_to_flat(menu_item):
                yield item
            yield {'end_node': True}

        yield {'end_nodes': True}
    else:
        yield {'link': node.link, 'data': node.value, 'is_data': True}
