from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, 'index1.html', {'movie_list': movies})


def details(request, movie_id):
    # return HttpResponse("This is movie number %s" % movie_id)
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details1.html', {'movie': movie})


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, img=img)
        if movie:
            movie.save()
            return redirect('/')
    return render(request, 'add1.html')


def update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit1.html', {'form': form, 'movie': movie})


def delete(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    # return render(request, 'delete.html')


