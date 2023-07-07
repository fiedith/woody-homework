from django.db import models
from users.models import User

class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=False)
    content = models.CharField(max_length=500, null=False)
