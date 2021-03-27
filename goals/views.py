from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Goal, Step, Reward, Profile
from .forms import CatForm, GoalForm, StepForm, RewardForm

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

def formsuccess(request):
    response=redirect('goals/formsuccess.html')
    return response

def newcat(request):
    form=CatForm
    if request.method=='POST':
        form=CatForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save
            return render(request, 'goals/formsuccess.html')
    else:
        form=CatForm()
    return render(request, 'goals/newcat.html', {'form' : form})

def newgoal(request):
    form=GoalForm()
    if request.method=='POST':
        form=GoalForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save
            return render(request, 'goals/formsuccess.html')
    else:
        form=GoalForm()
    return render(request, 'goals/newgoal.html', {'form': form})

def newstep(request):
    form=StepForm()
    if request.method=='POST':
        form=StepForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save
            return render(request, 'goals/formsuccess.html')
    else:
        form=StepForm()
    return render(request, 'goals/newstep.html', {'form': form})

def newreward(request):
    form=RewardForm()
    if request.method=='POST':
        form=RewardForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save
            return render(request, 'goals/formsuccess.html')
    else:
        form=RewardForm()
    return render(request, 'goals/newreward.html', {'form': form})