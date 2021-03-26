from django.shortcuts import render, get_object_or_404
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

#To display all the goals within 1 category:
#     allgoals=Goal.objects.all
#     cat1 = Goal.objects.filter(category=1)
#     return render(request, 'goals/cat1.html' , {'catgoals' : catgoals})

def catgoals(request, id):
    thiscat =  get_object_or_404(Category, pk=id)
    catgoals=Goal.objects.filter(category=id)
    context={
        'thiscat' : thiscat,
        'catgoals' : catgoals,
    }
    return render(request, 'goals/catgoals.html', context=context)

def gsteps(request, id):
    thisgoal= get_object_or_404(Goal, pk=id)
    gsteps=Step.objects.filter(goal=id)
    context={
        'thisgoal' : thisgoal,
        'gsteps' : gsteps,
    }
    return render(request, 'goals/gsteps.html', context=context)