from django.db import models

class Person(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  
class Lesson(models.Model):
  author_name = models.CharField(max_length=30)
  date = 
  subject = 
  writtenContent = 
  mediaContect = 
  
class PortfolioProject(models.Model):
  industry = models.CharField(max_length=30)
  mediaContent = 
  writtenContent = 
  
