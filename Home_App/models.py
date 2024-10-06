from django.db import models

# Create your models here.

class cvTemplateClass(models.Model):
    fullName = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    contactNumber = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    socialMediaLinks = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    education = models.TextField()
    experience = models.TextField()
    
    def __str__(self):
        return self.fullName
    
