from django.db import models

#class Person(models.Model):
  #first_name = models.CharField(max_length=30)
  #last_name = models.CharField(max_length=30)
  
class Lesson(models.Model):
  author_name = models.CharField(max_length=30)
  release_date = models.DateField()
  last_updated = models.DateField()
  SUBJECTS = (
        ('E', 'Education'),
        ('M', 'Market Research'),
        ('C', 'Carpentry'),
    )
  subject = models.CharField(max_length=1, choices=SUBJECTS)

  writtenContent = models.CharField(max_length=30)
 # mediaContect = 
  
#class PortfolioProject(models.Model):
 # industry = models.CharField(max_length=30)
 # mediaContent = 
  #writtenContent = models.CharField(max_length=30)
  
