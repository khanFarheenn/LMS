from django.db import models
# Create your models here.


class Books(models.Model):
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    publisher=models.CharField(max_length=250)
    number_of_book=models.BigIntegerField()

class Student(models.Model):
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    age=models.BigIntegerField()
    phone_number=models.BigIntegerField()


class Issue(models.Model):
    book_id=models.BigIntegerField()
    student_id=models.BigIntegerField()
    date=models.DateField()
    time=models.TimeField()    
    
    
    
class Manager(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=250)    
    
    
class Return_records(models.Model):
    book_id=models.BigIntegerField()
    student_id=models.BigIntegerField()
    date=models.DateField()
    time=models.TimeField()  
