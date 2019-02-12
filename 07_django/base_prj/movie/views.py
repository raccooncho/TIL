from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm, MovieModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = { 'movies': movies }
    return render(request, 'movie/index.html', context)


@login_required(login_url='/accounts/signin')
def create(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            # rpg = form.cleaned_data.get
            # movie = Movie()
            # movie.title = rpg('title')
            # movie.title_eng = rpg('title_eng')
            # movie.audience = rpg('audience')
            # movie.open_dt = rpg('open_dt')
            # movie.genre = rpg('genre')
            # movie.watch_grade = rpg('watch_grade')
            # movie.score = rpg('score')
            # movie.poster_url = rpg('poster_url')
            # movie.description = rpg('description')
            # movie.save()
            form.save()
            return redirect('movie:index')
    else:
        form = MovieModelForm()
        context = { 'form': form }
    return render(request, 'movie/create.html', context)


def update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:update', id)
    else:
        form = MovieModelForm(instance=movie)
        context = { 'form': form }
        return render(request, 'movie/update.html', context)


