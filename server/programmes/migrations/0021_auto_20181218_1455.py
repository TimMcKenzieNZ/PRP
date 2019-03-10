# Generated by Django 2.1.3 on 2018-12-18 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0020_auto_20181218_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(choices=[('No Role', 'No Role'), ('Consultant', 'Consultant'), ('Project Team Member', 'Project Team Member'), ('Project Manager', 'Project Manager'), ('Analyst', 'Analyst'), ('Client', 'Client'), ('Sponsor', 'Sponsor'), ('Administrator', 'Administrator'), ('Developer', 'Developer'), ('Support', 'Support'), ('Supplier', 'Supplier'), ('Stakeholder', 'Stakeholder'), ('Tester', 'Tester'), ('User', 'User'), ('Domain Expert', 'Domain Expert'), ('Quality Assurance', 'Quality Assurance'), ('Designer', 'Designer'), ('Technician', 'Technician'), ('Team Leader', 'Team Leader')], default='No Role', max_length=20),
        ),
    ]
