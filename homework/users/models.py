from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)

    # food for thought: cascade on posts and comments
    def delete(self):
        # delete user's posts
        self.board_set.all().delete()

        # delete user's comments
        self.comment_set.all().delete()

        # delete user
        super().delete()