# Generated by Django 2.1.3 on 2019-01-14 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0031_auto_20190114_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.CharField(choices=[('Very Low', 'Very Low'), ('Low', 'Low'), ('Moderate', 'Moderate'), ('High', 'High'), ('Very High', 'Very High')], default='Very Low', max_length=8),
        ),
        migrations.AlterField(
            model_name='risk',
            name='impact',
            field=models.CharField(choices=[('Very Low', 'Very Low'), ('Low', 'Low'), ('Moderate', 'Moderate'), ('High', 'High'), ('Very High', 'Very High')], default='Very Low', max_length=12),
        ),
        migrations.AlterField(
            model_name='risk',
            name='likelihood',
            field=models.CharField(choices=[('Very Low', 'Very Low'), ('Low', 'Low'), ('Moderate', 'Moderate'), ('High', 'High'), ('Very High', 'Very High')], default='Very Low', max_length=12),
        ),
        migrations.AlterField(
            model_name='riskcategory',
            name='impact',
            field=models.CharField(choices=[('Very Low', 'Very Low'), ('Low', 'Low'), ('Moderate', 'Moderate'), ('High', 'High'), ('Very High', 'Very High')], default=None, max_length=8),
        ),
        migrations.AlterField(
            model_name='riskcategory',
            name='likelihood',
            field=models.CharField(choices=[('Very Low', 'Very Low'), ('Low', 'Low'), ('Moderate', 'Moderate'), ('High', 'High'), ('Very High', 'Very High')], default=None, max_length=8),
        ),
    ]
