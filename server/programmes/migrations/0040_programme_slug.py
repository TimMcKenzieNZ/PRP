# Generated by Django 2.1.3 on 2019-01-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0039_auto_20190114_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='slug',
            field=models.CharField(max_length=30, unique=True),
            preserve_default=False,
        ),
    ]
