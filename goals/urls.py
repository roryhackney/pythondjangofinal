from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('getrewards/', views.getrewards, name='rewards'),
    path('getcategories/', views.getcategories, name='categories'),
    path('catgoals/<int:id>', views.catgoals, name='catgoals'),
    path('gsteps/<int:id>', views.gsteps, name='gsteps'),
]