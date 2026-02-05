from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_home, name='games_home'),  # <--- new
      path('flipcard/', views.flipcard, name='flipcard'),
    path('sudoku/', views.sudoku, name='sudoku'),
    path('hangman/', views.hangman, name='hangman'),
    path('draw/', views.draw_page, name='draw_page'),
]
