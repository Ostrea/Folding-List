from django.db import models


class Menu:
    # name = ''
    # items = []

    def __init__(self, name, link, items):
        self.name = name
        self.items = items
        self.link = link


class MenuItem:
    # value = ''
    # sub_items = []

    def __init__(self, value, link):
        self.value = value
        self.link = link
