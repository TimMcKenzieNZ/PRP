# Generated by Django 2.1.3 on 2019-01-09 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0026_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
