from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255, null=True, blank=True)
    motivation=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table='category'
        verbose_name_plural='categories'

class Goal(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255, null=True, blank=True)
    motivation=models.CharField(max_length=255, null=True, blank=True)
    timeline=models.DateField()
    points=models.IntegerField(default=300, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table="goal"
        verbose_name_plural="goals"
        ordering=["timeline"]

class Step(models.Model):
    class Choices(models.IntegerChoices):
        EASY=10
        MEDIUM=20
        HARD=30

    difficulty=models.IntegerField(choices=Choices.choices, default=Choices.EASY)
    
    goal=models.ForeignKey(Goal, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255, null=True, blank=True)
    timeline=models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        db_table="step"
        verbose_name_plural="steps"
        ordering=["timeline"]

class Reward(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255, null=True, blank=True)
    cost=models.SmallIntegerField(default=100)
    used=models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table="reward"
        verbose_name_plural="rewards"

class Profile(models.Model):
    points=models.PositiveSmallIntegerField(editable=False, default=0)
    displayname=models.CharField(max_length=255, default='DisplayName')

    def __str__(self):
        return self.displayname

    class Meta:
        db_table="profile"
        verbose_name_plural="profiles"