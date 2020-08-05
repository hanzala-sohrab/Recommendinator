from django import forms

class AnimeForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)