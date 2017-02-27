from django.db import models

# Create your models here.

class UserToken(models.Model):
    token = models.CharField(max_length=56)
    email = models.EmailField()
    month_count = models.IntegerField(default=0)


class EncLog(models.Model):
    enc_id = models.CharField(max_length=64)
    enc_info = models.TextField()
    # not DateTimeField
    saved_date = models.DateField()


class NewsScore(models.Model):
    name = models.CharField(max_length=50)
    news_id = models.CharField(max_length=50)

