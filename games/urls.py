from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),  
    path('game/', views.games_home, name='games_home'),
    path('flipcard/', views.flipcard, name='flipcard'),
    path('sudoku/', views.sudoku, name='sudoku'),
    path('hangman/', views.hangman, name='hangman'),
    path('math_quiz/', views.math_quiz, name='math_quiz'),
    path('draw/', views.draw_page, name='draw_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
