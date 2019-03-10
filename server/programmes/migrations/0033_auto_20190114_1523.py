# Generated by Django 2.1.3 on 2019-01-14 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0032_auto_20190114_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='benefits',
        ),
        migrations.AddField(
            model_name='benefit',
            name='goals',
            field=models.ManyToManyField(related_name='benefits', to='programmes.Goal'),
        ),
    ]
