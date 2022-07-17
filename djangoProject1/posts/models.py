from django.db import models


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
