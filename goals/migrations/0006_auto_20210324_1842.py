# Generated by Django 3.1.5 on 2021-03-25 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0005_category_goal_profile_reward_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='displayname',
            field=models.CharField(max_length=255),
        ),
    ]
