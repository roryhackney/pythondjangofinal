from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('getrewards/', views.getrewards, name='rewards'),
    path('getcategories/', views.getcategories, name='categories'),
    path('catgoals/<int:id>', views.catgoals, name='catgoals'),
    path('gsteps/<int:id>', views.gsteps, name='gsteps'),
    path('newcat/', views.newcat, name='newcat'),
    path('formsuccess/', views.formsuccess, name='formsuccess'),
    path('newgoal/', views.newgoal, name='newgoal'),
    path('newstep/', views.newstep, name='newstep'),
    path('newreward/', views.newreward, name='newreward'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]