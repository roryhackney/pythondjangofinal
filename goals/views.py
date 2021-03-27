from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Goal, Step, Reward, Profile
from .forms import CatForm, GoalForm, StepForm, RewardForm

# Create your views here.
def index(request):
    return render(request, 'goals/index.html')

@login_required
def getrewards(request):
    #rewardlist=Reward.objects.all()
    userrewards=Reward.objects.filter(user=request.user)
    return render(request, 'goals/rewards.html' , {'userrewards' : userrewards})

@login_required
def getcategories(request):
    #categorylist=Category.objects.all()
    usercats=Category.objects.filter(user=request.user)
    return render(request, 'goals/categories.html' ,{'usercats' : usercats})

#To display all the goals within 1 category:
#     allgoals=Goal.objects.all
#     cat1 = Goal.objects.filter(category=1)
#     return render(request, 'goals/cat1.html' , {'catgoals' : catgoals})

@login_required
def catgoals(request, id):
    thiscat =  get_object_or_404(Category, pk=id)
    catgoals=Goal.objects.filter(category=id)
    context={
        'thiscat' : thiscat,
        'catgoals' : catgoals,
    }
    return render(request, 'goals/catgoals.html', context=context)

@login_required
def gsteps(request, id):
    thisgoal= get_object_or_404(Goal, pk=id)
    gsteps=Step.objects.filter(goal=id)
    context={
        'thisgoal' : thisgoal,
        'gsteps' : gsteps,
    }
    return render(request, 'goals/gsteps.html', context=context)

@login_required
def formsuccess(request):
    response=redirect('goals/formsuccess.html')
    return response

@login_required
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

@login_required
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

@login_required
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

@login_required
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

def loginmessage(request):
    return render(request, 'goals/loginmessage.html')

def logoutmessage(request):
    return render(request, 'goals/logoutmessage.html')