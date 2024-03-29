# Generated by Django 2.1.3 on 2019-01-10 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0027_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Overdue', 'Overdue'), ('Complete', 'Complete'), ('In Progress', 'In Progress'), ('Not Started', 'Not Started'), ('Blocked', 'Blocked'), ('Deferred', 'Deferred'), ('Cancelled', 'Cancelled'), ('Delayed', 'Delayed')], default='Not Started', max_length=12),
        ),
    ]
