from django.db import models
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    phone = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(timezone.now)
    description = models.TextField(blank=True)
