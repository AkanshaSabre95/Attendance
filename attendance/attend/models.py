from django.db import models
from django.core.validators import MaxValueValidator

class Student(models.Model):
     WEEKDAYS = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
     
     STATUS_CHOICE = [
         (1, 'Present'),
         (2, 'Sickday'),
         (3, 'Vacation'),
         (4, 'Absent'),
         (5, 'Late'),
     ]


     CLASS_NAMES = [
        ('Nervous system', 'Nervous system'),
        ('First Aid','First Aid'),
        ('Pathology Class','Pathology Class')
    ]
     
     student_name = models.CharField(max_length=255)
     week_commencing = models.DateField()
     weekday = models.CharField(max_length=10, choices=WEEKDAYS)
     class_name = models.CharField(max_length=255, choices=CLASS_NAMES) 
     status = models.IntegerField(choices=STATUS_CHOICE)
     week_commencing = models.DateField()
     days_present = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
     days_absent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
     days_late = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
     instructor = models.CharField(max_length=255, blank=True, null=True)
     automation_button_clicked = models.BooleanField(default=False)

     def __str__(self):
        return self.student_name





  

