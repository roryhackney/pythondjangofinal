from django.contrib import admin
from .models import Category, Goal, Step, Reward, Profile

# Register your models here.
admin.site.register(Category)
admin.site.register(Goal)
admin.site.register(Step)
admin.site.register(Reward)
admin.site.register(Profile)