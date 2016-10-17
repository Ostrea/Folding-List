from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children')

    def __str__(self):
        return 'Name: {}, Link: {}'.format(self.name, self.link)
