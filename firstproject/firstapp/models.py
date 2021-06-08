from django.db import models

# Create your models here.
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


class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.fname