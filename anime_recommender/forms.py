from django import forms
from recommender import ANIMES

class AnimeForm(forms.Form):
    # name = forms.CharField(max_length=100, required=True, choices = ANIMES, default = "Naruto")
    name = forms.ChoiceField(choices=ANIMES)