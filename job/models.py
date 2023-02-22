from django.db import models
# Create your models here.


class InternData(models.Model):
    description = models.TextField(max_length=2000)
    intern_link = models.CharField(max_length=200)
    