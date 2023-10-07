from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Record(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=400)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
