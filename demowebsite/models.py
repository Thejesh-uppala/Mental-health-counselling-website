import email
from tokenize import Number
from django.db import models
from django.forms import PasswordInput

# Create your models here.
class UserMaster(models.Model):
    admin_email = models.EmailField(max_length=50)
    admin_password = models.CharField(max_length=50)


class Sregistered(models.Model):
    sid = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    sem = models.CharField(max_length=50)
    dname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    pin = models.CharField(max_length=10)
    phno = models.CharField(max_length=10)


class Semester(models.Model):
    s_sid = models.ForeignKey(Sregistered, related_name='semestersid', on_delete=models.CASCADE)
    s_sem = models.ForeignKey(Sregistered, related_name='semestersem', on_delete=models.CASCADE)

class Department(models.Model):
    d_sid = models.ForeignKey(Sregistered, related_name='departmentsid', on_delete=models.CASCADE)
    deptname = models.ForeignKey(Sregistered, related_name='departmentname', on_delete=models.CASCADE)


class Counsellor(models.Model):
    cid = models.CharField(primary_key=True, max_length=50)
    cname = models.CharField(max_length=50)
    key = models.CharField(max_length=10)


class Appointment(models.Model):
    status = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    s_email = models.ForeignKey(Sregistered, related_name='studentemail', on_delete=models.CASCADE)
    mssgs = models.CharField(max_length=100, null=True)
    s_name = models.ForeignKey(Sregistered, related_name='studentname', on_delete=models.CASCADE)
    student_id = models.ForeignKey(Sregistered, related_name='studentid', primary_key=True, on_delete=models.CASCADE)
    
    





