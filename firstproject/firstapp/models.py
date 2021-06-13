from django.db import models
from django.contrib.auth.models import User # Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topics = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateTimeField()
    
    def __str__(self):
        return str(self.date)


class Users(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.fname


class UserProfileInfor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return self.user.username


class School(models.Model):
    name = models.CharField(max_length=265)
    principal = models.CharField(max_length=265)
    location = models.CharField(max_length=265)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=265)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='Students',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name