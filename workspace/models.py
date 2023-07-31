from django.db import models
from django.contrib.auth.models import User

class Workspace (models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField()
    bookmarked = models.BooleanField(default=False, blank=True)
    # settings = 
        # To see element titles in admin ORM 
    def __str__(self):
        return self.title
    
class WorkspaceSetting (models.Model):
    pass

class Element (models.Model):
    title = models.CharField(max_length=100)
    content =  models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) 
    favourite = models.BooleanField(default=False, blank=True)

        # To see element titles in admin ORM 
    def __str__(self):
        return self.title
