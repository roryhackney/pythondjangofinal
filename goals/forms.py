from django import forms
from .models import Category, Goal, Step, Reward, Profile

class CatForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class GoalForm(forms.ModelForm):
    class Meta:
        model=Goal
        fields='__all__'

class StepForm(forms.ModelForm):
    class Meta:
        model=Step
        fields='__all__'

class RewardForm(forms.ModelForm):
    class Meta:
        model=Reward
        fields='__all__'