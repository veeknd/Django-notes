from django.db import models

# Create your models here.


class Record(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=400)
