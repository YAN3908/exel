from django.db import models

# Create your models here.

class Book(models.Model):
    Photo_Link = models.URLField(name='Photo Link', max_length=340)
    Name_of_event = models.CharField(name='Name of event', max_length=340, blank=True, null=True, default=None)

