from django.db import models

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=60)
#    mentor = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role': 'Mentor'}, related_name='students')

    def __str__(self):
        return self.student_name

class Internship(models.Model):
    id=models.IntegerField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    nature_of_work = models.CharField(max_length=255)
    reporting_authority = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    internship_mode = models.CharField(max_length=20)
    stipend = models.CharField(default="Yes",max_length=4)
    ppo = models.CharField(default="Yes",max_length=3)
    status = models.CharField(max_length=100)
    offer_letter = models.FileField(upload_to='offer_letters/', null=True, blank=True)

class Faculty(models.Model):

    faculty_id = models.IntegerField(primary_key=True)
    faculty_name = models.CharField(max_length=60)







# models.py

from django.db import models
from django.contrib.auth.models import User
class Announcement(models.Model):
    text = models.TextField()
    user = models.ForeignKey(Faculty, on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class InternshipResponse(models.Model):
    STATUS_CHOICES = [
        ('In progress', 'In progress'),
        ('Completed', 'Completed'),
    ]

    MODE_CHOICES = [
        ('Virtual', 'Virtual'),
        ('Physical', 'Physical'),
    ]

    STIPEND_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    digital_id = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    email_id = models.EmailField()
    alternate_email_id = models.EmailField(blank=True, null=True)
    mobile_no = models.CharField(max_length=15)
    organisation_name = models.CharField(max_length=255)
    organisation_address_website = models.TextField()
    nature_of_work = models.TextField()
    repr_name = models.CharField(max_length=255)
    repr_designation = models.CharField(max_length=255)
    repr_email_id = models.EmailField()
    repr_mobile_no = models.CharField(max_length=15)    
    start_date = models.DateField()
    completion_date = models.DateField()
    duration = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    mode_of_internship = models.CharField(max_length=10, choices=MODE_CHOICES)
    stipend = models.CharField(max_length=3, choices=STIPEND_CHOICES)
    stipend_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    offer_letter_submitted = models.TextField(default=None)
    completion_certificate_submitted = models.TextField(default=None)

class OD(models.Model):
    register_number = models.CharField(max_length=100)
    email_id = models.EmailField()
    organisation_name = models.CharField(max_length=255)
    approved=models.BooleanField(default=False)