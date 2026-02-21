from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import GameScore, Game
import random
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from django.core.files.base import ContentFile
from .models import Drawing
from .models import HomeImage


def home(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        description = request.POST.get('description', '')

        if image:
            HomeImage.objects.create(image=image, description=description)
            return redirect('home')

    images = HomeImage.objects.all()
    return render(request, 'games/home.html', {'images': images})

def games_home(request):
    games = Game.objects.all()                 
    top_scores = GameScore.objects.order_by('-score')[:5]  
    return render(request, 'games/game.html', {
        'games': games,
        'top_scores': top_scores
    })


@login_required
def flipcard(request):
    game = Game.objects.get(url_name="flipcard")  

    if request.method == "POST":
        score = int(request.POST.get("score", 0))
        GameScore.objects.create(user=request.user, game=game, score=score)
        return redirect('games_home')  

    return render(request, 'games/flipcard.html', {
        'game_name': game.name
    })


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Game, GameScore

@login_required
def sudoku(request):
    game = Game.objects.get(url_name="sudoku") 

    if request.method == "POST":
        score = int(request.POST.get("score", 0))
        GameScore.objects.create(user=request.user, game=game, score=score)
        return redirect('games_home') 

    puzzle = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9],
    ]
    return render(request, 'games/sudoku.html', {'puzzle': puzzle, 'game_name': game.name})



# WORDS = ["apple", "banana", "mango", "carrot", "onion"]
@login_required
def hangman(request):
  
    game = Game.objects.get(url_name="hangman")  

    if request.method == "POST":
        score = int(request.POST.get("score", 0))
        # Save score for current user
        GameScore.objects.create(user=request.user, game=game, score=score)
        return redirect('games_home') 

   
    return render(request, 'games/hangman.html', {
        'game_name': game.name
    })

@login_required
@csrf_exempt
def draw_page(request):
    if request.method == "POST":
        data = request.POST.get("image")
        if data:
            format, imgstr = data.split(';base64,') 
            ext = format.split('/')[-1] 
            file_data = ContentFile(base64.b64decode(imgstr), name=f"drawing.{ext}")
            Drawing.objects.create(user=request.user, image=file_data)
            return JsonResponse({"success": True})
        return JsonResponse({"success": False})
    return render(request, 'games/draw.html', {'game_name': 'Easy Draw'})


@login_required
def math_quiz(request):
    game = Game.objects.get(url_name="math_quiz")

    a = random.randint(1, 20)
    b = random.randint(1, 20)

    if request.method == "POST":
        score = int(request.POST.get("score", 0))
        GameScore.objects.create(
            user=request.user,
            game=game,
            score=score
        )
        return redirect('games_home')

    return render(request, 'games/math_quiz.html', {
        'game_name': game.name,
        'a': a,
        'b': b
    })


