from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
