from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Upload(models.Model):
    docTitle = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    upload_date = models.DateTimeField(default=timezone.now)
    file = models.FileField()

