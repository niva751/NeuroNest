from django.db import models
from django.contrib.auth.models import User

class GameScore(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    game_name = models.CharField(max_length=50)
    score = models.IntegerField()
