from django.db import models


class Menu:

    def __init__(self, name, link, items=None):
        self.name = name
        self.link = link
        self.items = items
