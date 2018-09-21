from __future__ import unicode_literals
from django.db import models

class ProductGroup(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(to='ProductGroup', null=True, 
                               related_name='subgroups', 
                               on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    group = models.ForeignKey(to='ProductGroup', on_delete=models.CASCADE)
    pic = models.ImageField(upload_to = 'catalogimages', null = True, 
                            blank=True)

    def __str__(self):
        return self.name

    def get_group_name(self):
        return self.group.name
