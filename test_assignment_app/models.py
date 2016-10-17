from django.db import models


class Menu:
    # name = ''
    # items = []

    def __init__(self, name, items=None):
        self.name = name
        self.items = items


class MenuItem:
    # value = ''
    # sub_items = []

    def __init__(self, value):
        self.value = value
