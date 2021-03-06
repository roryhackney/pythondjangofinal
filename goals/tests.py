from django.test import TestCase
from .models import Category, Goal, Step, Reward, Profile
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from .views import index, getrewards, getcategories, catgoals, gsteps
from .forms import CatForm, GoalForm, StepForm, RewardForm
from django import forms

# Create your tests here.

#MODEL TESTING##########################################

class CategoryTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username="bob5", password="P@ssw0rd9")
        self.type=Category.objects.create(title="TestCategory", description="Test category", motivation="For testing", user=self.u)

    def testString(self):
        self.assertEqual(str(self.type), self.type.title)

    def testTable(self):
        self.assertEqual(str(Category._meta.db_table), 'category')

class GoalTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username="alex1", password='P@ssw0rd9')
        self.cat=Category.objects.create(title="TestCat", description="test", motivation="testing", user=self.u)
        self.goal=Goal.objects.create(title="TestGoal", description="Test goal", motivation="For testing", category=self.cat, timeline=datetime.date(2021, 3, 27))

    def testString(self):
        self.assertEqual(str(self.goal), self.goal.title)

    def testTable(self):
        self.assertEqual(str(Goal._meta.db_table), 'goal')

    def testCat(self):
        self.assertEqual(str(self.goal.category), 'TestCat')

class StepTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username="adam4", password='P@ssw0rd9')
        self.cat=Category.objects.create(title="TCat", description="testing", motivation="For testing", user=self.u)
        self.goal=Goal.objects.create(title="TGoal", description="Testing", motivation="For testing", category=self.cat, timeline=datetime.date(2022, 5, 27))
        self.step=Step.objects.create(title='Step Test', description='Step testing', timeline=datetime.date(2021, 3, 30), difficulty=10, goal=self.goal)

    def testString(self):
        self.assertEqual(str(self.step), self.step.title)

    def testTable(self):
        self.assertEqual(str(Step._meta.db_table), 'step')

    def testGoal(self):
        self.assertEqual(str(self.step.goal), 'TGoal')

class RewardTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username="hannah2", password='P@ssw0rd9')
        self.reward=Reward.objects.create(title='Test Reward', description="Testing reward", cost=300, user=self.u)

    def testString(self):
        self.assertEqual(str(self.reward), self.reward.title)

    def testTable(self):
        self.assertEqual(str(self.reward._meta.db_table), 'reward')

class ProfileTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username="helen4", password='P@ssw0rd9')
        self.profile=Profile.objects.create(user=self.u, displayname='Bob')

    def testString(self):
        self.assertEqual(str(self.profile), self.profile.displayname)

    def testTable(self):
        self.assertEqual(str(self.profile), self.profile.displayname)

#After implementing login, pages can't be accessed without a user
#See authorization testing below

#FORM TESTING#################################

class CategoryFormTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username="bob74", password="P@ssw0rd9")
        
    def testFullValid(self):
        form=CatForm(data={"title": "NewCatTest", "description": "A test", "motivation": "To test New Category form", "user": self.u})
        self.assertTrue(form.is_valid())

    def testPartialDataValid(self):
        form=CatForm(data={"title": "PartCatTest", "user": self.u})
        self.assertTrue(form.is_valid())

    def testMissingData(self):
        form=CatForm(data={"title":"", "user": self.u})
        self.assertFalse(form.is_valid())

class GoalFormTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username="bob74", password="P@ssw0rd9")
        self.category=Category.objects.create(title="Test Cat", user=self.u)

    def testFullValid(self):
        form=GoalForm(data={"title": "NewGoalTest", "description": "A test", "motivation": "To test New Goal form", "timeline": datetime.date(2021, 6, 2), "category": self.category})
        self.assertTrue(form.is_valid())

    def testPartialDataValid(self):
        form=GoalForm(data={"title": "NewGoalTest", "timeline": datetime.date(2021, 6, 2), "category": self.category})        
        self.assertTrue(form.is_valid())

    def testMissingData(self):
        form=GoalForm(data={"title":""})
        self.assertFalse(form.is_valid())

class StepFormTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username="bob74", password="P@ssw0rd9")
        self.category=Category.objects.create(title="Test Cat", user=self.u)
        self.goal=Goal.objects.create(title='Test Goal', category=self.category, timeline=datetime.date(2023, 1, 4))

    def testFullValid(self):
        form=StepForm(data={"title": "NewStepTest", "description": "A test", "timeline": datetime.date(2021, 6, 2), "goal": self.goal, "difficulty": 10})
        self.assertTrue(form.is_valid())

    def testPartialDataValid(self):
        form=StepForm(data={"title": "NewStepTest", "timeline": datetime.date(2021, 6, 2), "goal": self.goal, "difficulty":20})
        self.assertTrue(form.is_valid())

    def testMissingData(self):
        form=StepForm(data={"title":""})
        self.assertFalse(form.is_valid())


#PAGE TESTING (NO AUTH)###################################

class IndexTest(TestCase):
    def testUrlAccessedByName(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

#AUTHENTICATION TESTING#####################################

class ViewCatAuth(TestCase):
    def setUp(self):
        self.u=User.objects.create_user(username='bean4', password='P@ssw0rd9')
        self.u.save()
        self.cat=Category.objects.create(title="AuthCat", user=self.u)

#Doesn't work without auth, replaced by testLoginRightTemplate()
    #class CatPageTest(TestCase):
        # def testUrlAccessedByName(self):
        #     response=self.client.get(reverse('categories'))
        #     self.assertEqual(response.status_code, 200)

    def testRedirectNoLogin(self):
        response=self.client.get(reverse('categories'))
        self.assertRedirects(response, '/accounts/login/?next=/goals/getcategories/')

    def testLoginRightTemplate(self):
        login=self.client.login(username='bean4', password='P@ssw0rd9')
        response=self.client.get(reverse('categories'))
        self.assertEqual(str(response.context['user']), 'bean4')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goals/categories.html')

class ViewRewardAuth(TestCase):
    def setUp(self):
        self.u=User.objects.create_user(username='bean4', password='P@ssw0rd9')
        self.u.save()
        self.reward=Reward.objects.create(title='Test Reward', user=self.u, cost=150)

    def testRedirectNoLogin(self):
        response=self.client.get(reverse('rewards'))
        self.assertRedirects(response, '/accounts/login/?next=/goals/getrewards/')

    def testLoginRightTemplate(self):
        login=self.client.login(username='bean4', password='P@ssw0rd9')
        response=self.client.get(reverse('rewards'))
        self.assertEqual(str(response.context['user']), 'bean4')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goals/rewards.html')

class CatGoalsAuth(TestCase):
    def setUp(self):
        self.u=User.objects.create_user(username='bean4', password='P@ssw0rd9')
        self.u.save()
        # self.u=User.objects.create(username="armando1", password='P@ssw0rd9')
        self.cat=Category.objects.create(title='Catgoals Test', description="Test Catgoals page", motivation='For testing', user=self.u)
        self.goals=Goal.objects.create(title='Catgoals Goal Test', description='Subgoals', motivation='For testing Catgoals subgoals', category=self.cat, timeline=datetime.date(2023, 5, 19))

    # def testDetailAccessedUsingID(self):
    #     response=self.client.get(reverse('catgoals', args=(self.cat.id,)))
    #     self.assertEqual(response.status_code, 200)
    
    def testNumGoals(self):
        self.goalnum=Goal.objects.filter(category=self.cat).count()
        self.assertEqual(self.goalnum, 1)

    def testRedirectNoLogin(self):
        response=self.client.get(reverse('catgoals', args=(self.cat.id,)))
        self.assertRedirects(response, '/accounts/login/?next=/goals/catgoals/' + str(self.cat.id))

    def testLoginRightTemplate(self):
        login=self.client.login(username='bean4', password='P@ssw0rd9')
        response=self.client.get(reverse('catgoals', args=(self.cat.id,)))
        self.assertEqual(str(response.context['user']), 'bean4')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goals/catgoals.html')

class GstepsAuth(TestCase):
    def setUp(self):
        self.u=User.objects.create_user(username='bean4', password='P@ssw0rd9')
        self.u.save()
        self.cat=Category.objects.create(title='Gsteps Cat Test', description="Test Catgoals page", motivation='For testing', user=self.u)
        self.goals=Goal.objects.create(title='Gsteps Goal Test', description='Subgoals', motivation='For testing Catgoals subgoals', category=self.cat, timeline=datetime.date(2023, 5, 19))
        self.steps=Step.objects.create(title='Gteps Steps Test 1', timeline=datetime.date(2021, 1, 15), difficulty=10, goal=self.goals)
        self.steps2=Step.objects.create(title='Gteps Steps Test 2', timeline=datetime.date(2023, 1, 15), difficulty=20, goal=self.goals)

    # def testDetailAccessedUsingID(self):
    #     response=self.client.get(reverse('gsteps', args=(self.goals.id,)))
    #     self.assertEqual(response.status_code, 200)
    
    def testNumGoals(self):
        self.stepnum=Step.objects.filter(goal=self.goals).count()
        self.assertEqual(self.stepnum, 2)

    def testRedirectNoLogin(self):
        response=self.client.get(reverse('gsteps', args=(self.goals.id,)))
        self.assertRedirects(response, '/accounts/login/?next=/goals/gsteps/' + str(self.goals.id))

    def testLoginRightTemplate(self):
        login=self.client.login(username='bean4', password='P@ssw0rd9')
        response=self.client.get(reverse('gsteps', args=(self.goals.id,)))
        self.assertEqual(str(response.context['user']), 'bean4')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goals/gsteps.html')