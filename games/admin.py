from django.contrib import admin

# Register your models here.
from .models import Game, GameScore, Drawing, HomeImage

admin.site.register(Game)
admin.site.register(GameScore)
admin.site.register(Drawing)
admin.site.register(HomeImage)
