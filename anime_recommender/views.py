from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import AnimeForm
from .models import Anime, Rating
from recommender import print_similar_animes

# Create your views here.
class Index(FormView):
    template_name = 'anime_recommender/index.html'
    form_class = AnimeForm  

    def form_valid(self, form):
        anime = form.cleaned_data.get('name')
        print("Hello12")
        anime = anime.replace(' ', '-')
        return redirect('anime', anime)


def anime_recommend(request, anime):
    # anime = Anime.objects.filter(name = anime).values_list('name', flat=True)[0]
    anime = anime.replace('-', ' ')
    similar_animes = print_similar_animes(anime)
    return render(request, 'anime_recommender/anime.html', {'anime': anime, 'suggestions': similar_animes})