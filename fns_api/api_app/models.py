from django.db import models

# Create your models here.

class UserToken(models.Model):
    token = models.CharField(max_length=56)
    email = models.EmailField()
    month_count = models.IntegerField(default=0)

