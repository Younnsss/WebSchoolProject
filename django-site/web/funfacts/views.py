# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import VideoGame, Vote

def video_games_list(request):
    video_games = VideoGame.objects.annotate_with_total_votes().order_by('-created_at')
    return render(request, 'funfacts/video_games_list.html', {'video_games': video_games})

@login_required
def create_video_game(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        VideoGame.objects.create(title=title, description=description, author=request.user)
        return redirect('video_games_list')
    return render(request, 'funfacts/create_video_game.html')

@login_required
def vote_video_game(request, video_game_id, vote_value):
    video_game = get_object_or_404(VideoGame, id=video_game_id)
    vote, created = Vote.objects.get_or_create(user=request.user, video_game=video_game,
        defaults={'value': float(vote_value)})
    vote.value = float(vote_value)
    vote.save()
    return redirect('video_games_list')