# api/views.py

from front.models import VideoGame, Vote
from django.http import JsonResponse

def video_games_all(request):
    video_games = VideoGame.objects.annotate_with_total_votes().order_by('-created_at')
    video_games_list = list(video_games.values('id', 'title', 'description', 'author__username', 'created_at', 'total_votes'))
    return JsonResponse(video_games_list, safe=False)


def votes_all(request):
    votes = Vote.objects
    votes_list = list(votes.values('id', 'user', 'video_game', 'value'))
    return JsonResponse(votes_list, safe=False)

