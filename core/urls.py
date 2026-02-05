from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('memory/',views.memory,name='memory'),
    path('logout/',views.logout_view,name='logout'),
    path('ml/draw/',views.ml_draw,name='ml_draw'),
]
