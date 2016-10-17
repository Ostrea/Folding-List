from django import template


register = template.Library()


@register.inclusion_tag('test_assignment_app/menu.html')
def draw_menu(menu_name):
    choices = ['one', 'two', 'three']
    return {'choices': choices}
