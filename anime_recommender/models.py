from django.db import models

# Create your models here.
class Anime(models.Model):
    anime_id = models.IntegerField()
    name = models.CharField(max_length=100, null=False)
    genre = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    episodes = models.IntegerField()
    rating = models.IntegerField()
    members = models.IntegerField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    user_id = models.IntegerField()
    anime_id = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.rating
    