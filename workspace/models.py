from django.db import models
from django.contrib.auth.models import User

class Workspace(models.Model):
    id = models.AutoField(primary_key=True)  # Add an auto-incrementing ID field as the primary key
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='workspaces/logos/')  # This specifies the upload path for the logo images.
    bookmarked = models.BooleanField(default=False, blank=True)
    
    def __str__(self):
        return self.title

    

# class Element (models.Model):
#     title = models.CharField(max_length=100)
#     content =  models.TextField(blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True) 
#     favourite = models.BooleanField(default=False, blank=True)

#     # ForeignKey for the relationship
#     workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)  
#         # To see element titles in admin ORM 
#     def __str__(self):
#         return self.title
