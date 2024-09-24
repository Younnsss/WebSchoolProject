# funfacts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FunFact, Vote

def funfacts_list(request):
    funfacts = FunFact.objects.annotate_with_total_votes().order_by('-created_at')
    return render(request, 'funfacts/funfacts_list.html', {'funfacts': funfacts})

@login_required
def create_funfact(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        funfact = FunFact.objects.create(title=title, content=content, author=request.user)
        return redirect('funfacts_list')
    return render(request, 'funfacts/create_funfact.html')

@login_required
def vote_funfact(request, funfact_id, vote_value):
    funfact = get_object_or_404(FunFact, id=funfact_id)
    vote, created = Vote.objects.update_or_create(
        user=request.user, fun_fact=funfact,
        defaults={'value': float(vote_value)}
    )
    vote.save()
    return redirect('funfacts_list')
