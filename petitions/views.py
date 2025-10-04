from django.shortcuts import render, redirect, get_object_or_404
from .models import MoviePetition, PetitionVote

def index(request):
    petitions = MoviePetition.objects.all()
    template_data = {}
    template_data['title'] = 'Movie Petitions'
    template_data['petitions'] = petitions
    return render(request, 'petitions/index.html', {'template_data': template_data})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if title and description:
            MoviePetition.objects.create(title=title, description=description)
            return redirect('petitions.index')
    
    template_data = {'title': 'Create Petition'}
    return render(request, 'petitions/create.html', {'template_data': template_data})

def upvote(request, petition_id):
    petition = get_object_or_404(MoviePetition, id=petition_id)
    PetitionVote.objects.create(petition=petition)
    petition.vote_count += 1
    petition.save()
    return redirect('petitions.index')