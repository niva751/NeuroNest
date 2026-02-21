from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='games/icons/')
    url_name = models.CharField(max_length=50, help_text="Django URL name")

    def __str__(self):
        return self.name

class GameScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.game.name} : {self.score}"


from django.db import models
from django.contrib.auth.models import User

class Drawing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='drawings/')
    created_at = models.DateTimeField(auto_now_add=True)


class HomeImage(models.Model):
    image = models.ImageField(upload_to='home_images/')
    description = models.TextField(blank=True, help_text="Optional description for the image")

    def __str__(self):
        return self.name
