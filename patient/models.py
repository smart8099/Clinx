from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.utils.timezone import now
from  django.conf import settings


# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
       
)
    
class PatientInfo(models.Model):
    # patients personal info

    
   

    

    

    LEVEL_OF_STUDENT_CHOICE = (
        ('LEVEL 100', 'LEVEL 100'),
        ('LEVEL 200', 'LEVEL 200'),
        ('LEVEL 300', 'LEVEL 300'),
    )

    STUDENT_SESSION_CHOICES = (
        ('MORNING', 'Morning'),
        ('WEEKEND', 'Weekend')
    )

    
   
   

    DEPARTMENTS_IN_SCHOOL_CHOICES = (
        ('Accounting', 'Accounting'),
        ('Automobile Engineering', 'Automobile Engineering'),
        ('Biomedical Engineering', 'Biomedical Engineering'),
        ('Building Technology', 'Building Technology'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Computer Network Management', 'Computer Network Management'),
        ('Computer Science', 'Computer Science'),
        ('Electrical/Electronic Engineering', 'Electrical/Electronic Engineering'),
        ('Environmental Management and Technology', 'Environmental Management and Technology'),
        ('Fashion Design and Textiles', 'Fashion Design and Textiles'),
        ('Food  Technology', 'Food  Technology'),

        ('Graphic  Design', 'Graphic  Design'),
        ('Hospitality  Management', 'Hospitality  Management'),
        ('Marketing', 'Marketing'),

        ('Mechanical  Engineering', 'Mechanical  Engineering'),
        ('Medical Laboratory  Science', 'Medical Laboratory  Science'),
        ('Post Harvest Technology', 'Post Harvest Technology'),
        ('Purchasing and  Supply', 'Purchasing and  Supply'),
        ('Renewable Energy and System Engineering', 'Renewable Energy and System Engineering'),
        ('Secretarialship and  Management', 'Secretarialship and  Management'),
        ('Statistics', 'Statistics'),
    )
    First_name = models.CharField(max_length = 30)
    Last_name = models.CharField(max_length=30)
    Index_number = models.CharField(max_length=30,primary_key=True)
    Student_email = models.EmailField(max_length=50)
    Student_phone = models.CharField(max_length =11)
    Student_age = models.IntegerField()
    Student_gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    Student_department = models.CharField(max_length=39,choices=DEPARTMENTS_IN_SCHOOL_CHOICES) 
    Student_session = models.CharField(max_length=8,choices=STUDENT_SESSION_CHOICES)
    Student_level = models.CharField(max_length=9, choices=LEVEL_OF_STUDENT_CHOICE)
    Time_created = models.DateTimeField(default=now)


    
    def __str__():
        return self.index_number


class OPD(models.Model):
    student = models.ForeignKey(PatientInfo,on_delete=models.CASCADE, related_name ='opd')    
    weight = models.IntegerField()
    temperature = models.IntegerField()
    complains =models.TextField(max_length=400)
    date =models.DateTimeField(default=now)        

          


