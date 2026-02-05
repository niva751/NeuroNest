from django.shortcuts import render

def games_home(request):
    return render(request, 'games/home.html')

def flipcard(request):
    return render(request, 'games/flipcard.html')

# games/views.py
from django.shortcuts import render

def sudoku(request):
    # यो sample puzzle हो, 0 means empty
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
    return render(request, 'games/sudoku.html', {'puzzle': puzzle})


def hangman(request):
    return render(request, 'games/hangman.html')

def draw_page(request):
    return render(request, 'games/draw.html')


def games_home(request):
    return render(request, 'games/home.html')  # create this template
