# Generated by Django 2.1.3 on 2019-01-14 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0030_remove_goal_initiatives'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='projects',
        ),
        migrations.AddField(
            model_name='project',
            name='goals',
            field=models.ManyToManyField(related_name='projects', to='programmes.Goal'),
        ),
    ]
