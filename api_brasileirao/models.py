from django.db import models
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Team(models.Model):
    code = models.CharField(primary_key=True, max_length=3)
    name = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    matches = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    defeats = models.IntegerField(default=0)
    gf = models.IntegerField(default=0)
    ga = models.IntegerField(default=0)
    gd = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)

    permission_class = (IsAuthenticatedOrReadOnly,)

    def __str__(self):
        return self.name
