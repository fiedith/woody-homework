from django.db import models

from users.models import User


class Board(models.Model):
    # author as FK
    title = models.CharField(max_length=30, null=False)
    content = models.CharField(max_length=500, null=False)
    user_id = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, db_column="user_id")
