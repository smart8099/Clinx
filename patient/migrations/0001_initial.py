# Generated by Django 3.2 on 2021-04-12 22:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('First_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('Index_number', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Student_email', models.EmailField(max_length=50)),
                ('Student_phone', models.CharField(max_length=11)),
                ('Student_age', models.IntegerField()),
                ('Student_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
                ('Student_department', models.CharField(choices=[('Accounting', 'Accounting'), ('Automobile Engineering', 'Automobile Engineering'), ('Biomedical Engineering', 'Biomedical Engineering'), ('Building Technology', 'Building Technology'), ('Civil Engineering', 'Civil Engineering'), ('Computer Network Management', 'Computer Network Management'), ('Computer Science', 'Computer Science'), ('Electrical/Electronic Engineering', 'Electrical/Electronic Engineering'), ('Environmental Management and Technology', 'Environmental Management and Technology'), ('Fashion Design and Textiles', 'Fashion Design and Textiles'), ('Food  Technology', 'Food  Technology'), ('Graphic  Design', 'Graphic  Design'), ('Hospitality  Management', 'Hospitality  Management'), ('Marketing', 'Marketing'), ('Mechanical  Engineering', 'Mechanical  Engineering'), ('Medical Laboratory  Science', 'Medical Laboratory  Science'), ('Post Harvest Technology', 'Post Harvest Technology'), ('Purchasing and  Supply', 'Purchasing and  Supply'), ('Renewable Energy and System Engineering', 'Renewable Energy and System Engineering'), ('Secretarialship and  Management', 'Secretarialship and  Management'), ('Statistics', 'Statistics')], max_length=39)),
                ('Student_session', models.CharField(choices=[('MORNING', 'Morning'), ('WEEKEND', 'Weekend')], max_length=8)),
                ('Student_level', models.CharField(choices=[('LEVEL 100', 'LEVEL 100'), ('LEVEL 200', 'LEVEL 200'), ('LEVEL 300', 'LEVEL 300')], max_length=9)),
                ('Time_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='OPD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('complains', models.TextField(max_length=400)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opd', to='patient.patientinfo')),
            ],
        ),
    ]
