from django.db import models
from boards.models import Board
from users.models import User

class Comment(models.Model):
    content = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # only one comment per post: 1:1 relationship
    board = models.OneToOneField(Board, on_delete=models.CASCADE)
