from django.shortcuts import render
import requests

def index(request):

    movies = requests.get("http://172.30.4.81/movie/").json()

    return render(request, 'index.html', {'movies': movies})

def about(request):
    return render(request, 'about.html')

def detail(request, movie_id):

    request_url = "http://172.30.4.81/movie/" + movie_id
    movie = requests.get(request_url).json()

    return render(request, 'detail.html', {'movie': movie})
