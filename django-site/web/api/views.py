# api/views.py

from funfacts.models import FunFact, Vote
from django.http import JsonResponse

def funfacts_all(request):
    funfacts = FunFact.objects.annotate_with_total_votes().order_by('-created_at')
    funfacts_list = list(funfacts.values('id', 'title', 'content', 'author__username', 'created_at', 'total_votes'))
    return JsonResponse(funfacts_list, safe=False)


def votes_all(request):
    votes = Vote.objects
    votes_list = list(votes.values('id', 'user', 'fun_fact', 'value'))
    return JsonResponse(votes_list, safe=False)


