from django.db import models

# Create your models here.

class Book(models.Model):
    photo_link = models.URLField(max_length=340)
    name_of_event = models.CharField(max_length=540, blank=True, null=True, default=None)
    date_of_event = models.CharField(max_length=540, blank=True, null=True, default=None)
    description = models.CharField(max_length=540, blank=True, null=True, default=None)
    start_time = models.CharField(max_length=40, blank=True, null=True, default=None)
    end_time = models.CharField(max_length=40, blank=True, null=True, default=None)
    location_name= models.CharField(max_length=150, blank=True, null=True, default=None)
    first_event_category= models.CharField(max_length=350, blank=True, null=True, default=None)
    second_category = models.CharField( max_length=350, blank=True, null=True, default=None)
    free_or_Paid = models.CharField( max_length=350, blank=True, null=True, default=None)
    ticket_site_link= models.URLField(max_length=340, blank=True, null=True,)