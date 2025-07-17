from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    university = models.CharField(max_length=100, blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name