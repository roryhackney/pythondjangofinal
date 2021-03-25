from django.shortcuts import render
from .models import Category, Goal, Step, Reward, Profile

# Create your views here.
def index(request):
    return render(request, 'goals/index.html')

def getrewards(request):
    rewardlist=Reward.objects.all()
    return render(request, 'goals/rewards.html' , {'rewardlist' : rewardlist})

def getcategories(request):
    categorylist=Category.objects.all()
    return render(request, 'goals/categories.html' ,{'categorylist' : categorylist})