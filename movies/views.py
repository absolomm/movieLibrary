from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, CreateView
from .forms import MovieForm

from django.urls import reverse_lazy

from django.utils import timezone

from django import forms

from .models import movies

def home(request):
    video = movies.objects.all()
    return render(request, 'movies/home.html', {'video':video})

def AddMovie(request):
    if request.method == 'POST':
        if request.FILES['Movie_Icon'] and request.POST['Name'] and request.POST['Type'] and request.FILES['Movie_File'] and request.POST['Client'] and request.POST['Project_Manager']:
            Movie = movies()
            Movie.Movie_Icon = request.FILES['Movie_Icon']
            Movie.Name = request.POST['Name']
            Movie.Type = request.POST['Type']
            Movie.Movie_File = request.FILES['Movie_File']
            Movie.Client = request.POST['Client']
            Movie.Project_Manager = request.POST['Project_Manager']
            Movie.Creation_Date = timezone.datetime.now()
            Movie.Modified_Date = timezone.datetime.now()
            Movie.save()
            return redirect('home')
        else:
            return render(request, 'AddMovie.html', {'error': 'All fields are required!'})
    else:
        return render(request, 'AddMovie.html')

def ModifyMovie(request, pk):
    video = movies.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance = video)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm(instance = video)
        return render(request, 'movies/ModifyMovie.html', {'form': form})

def DeleteMovie(request, pk):
    if request.method == 'POST':
        video = movies.objects.get(pk=pk)
        video.delete()
    return redirect('home')

def MoviePlayer(request, movie_id):
    moviedetail=get_object_or_404(movies, pk=movie_id)
    return render(request, 'movies/MoviePlayer.html', {'movie': moviedetail})
