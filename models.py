from django.db import models

#class Person(models.Model):
  #first_name = models.CharField(max_length=30)
  #last_name = models.CharField(max_length=30)
  
class SiteUpdate(models.Model):
  #this SiteUpdate model is intended to advertise newly added features of the application.
  release_date = models.DateField()
  written_content = models.CharField(max_length=150)
  
  
class Lesson(models.Model):
  #this Lesson model is intended for efficienct publishing. Teachers may upload written content such as lessons for students to view and learn from. Lessons are identified by
  #author, lesson title, subject, release date, and last updated. By reusing the skeleton of a lesson, teachers are able to focus more on creativity.  
  author_name = models.CharField(max_length=30)
  lesson_title = models. CharField(max_length=15)
  SUBJECTS = (
        ('E', 'Education'),
        ('M', 'Market Research'),
        ('C', 'Carpentry'),
    )
  subject = models.CharField(max_length=1, choices=SUBJECTS)
  
  release_date = models.DateField()
  last_updated = models.DateField()
  
  writtenContent = models.CharField(max_length=30)

 # mediaContect = 
  
#class PortfolioProject(models.Model):
 # industry = models.CharField(max_length=30)
 # mediaContent = 
  #writtenContent = models.CharField(max_length=30)
  
