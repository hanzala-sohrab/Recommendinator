from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    # path('', views.index, name="index"),
    re_path(r'^anime/(?P<anime>[-\w]+)$', views.anime_recommend, name="anime"),
]