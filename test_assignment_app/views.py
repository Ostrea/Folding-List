from django.shortcuts import render
from django.http import Http404


def index(request):
    menu_name = request.GET.get('menu_name')
    active_item = None
    if menu_name:
        active_item = request.GET.get('active_item')
        if not active_item:
            raise Http404

    return render(request, 'test_assignment_app/index.html', {
        'request_menu_name': menu_name,
        'active_item': active_item
    })
