from django.db import models

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=100)
    urgent = models.BooleanField(null=True, blank=True)