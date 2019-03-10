# Generated by Django 2.1.3 on 2018-12-18 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0021_auto_20181218_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='initiatives',
            field=models.ManyToManyField(related_name='roles', to='programmes.Initiative'),
        ),
        migrations.AlterField(
            model_name='role',
            name='teammembers',
            field=models.ManyToManyField(related_name='roles', to='programmes.TeamMember'),
        ),
    ]
