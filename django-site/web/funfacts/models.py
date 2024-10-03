# models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class VideoGameQuerySet(models.QuerySet):
    def annotate_with_total_votes(self):
        return self.annotate(total_votes=Sum("vote__value"))

class VideoGame(models.Model):
    objects = VideoGameQuerySet.as_manager()
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)
    value = models.IntegerField()  # 1 for upvote, -1 for downvote
    created_at = models.DateTimeField(auto_now_add=True)