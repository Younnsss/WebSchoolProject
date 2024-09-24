# funfacts/models.py

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum



class FunFactQuerySet(models.QuerySet):
    def annotate_with_total_votes(self):
        return self.annotate(total_votes=Sum("votes__value"))


class FunFact(models.Model):
    objects = FunFactQuerySet.as_manager()

    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Vote(models.Model):
    VOTE_CHOICES = [
        (1.0, 'Upvote'),
        (-1.0, 'Downvote'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fun_fact = models.ForeignKey(FunFact, related_name='votes', on_delete=models.CASCADE)
    value = models.FloatField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'fun_fact')
