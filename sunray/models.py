

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_details = models.TextField(default='')
    image = models.ImageField(upload_to='projects')  # Assuming you upload images to 'media/projects'
    date_created = models.DateField(auto_now_add=True)
    # Add any other fields you need

    def __str__(self):
        return self.title


class LargeProject(models.Model):
    title = models.CharField(max_length=100)
    kw=models.CharField(max_length=100,default='')
    place=models.CharField(max_length=100,default='')
    image = models.ImageField(upload_to='large_projects')  # Upload image to 'media/large_projects'
    date_created = models.DateField(auto_now_add=True)
    technology=models.CharField(max_length=100,default='')
    saves=models.CharField(max_length=50,default='')
    trees=models.CharField(max_length=50,default='')
    tons=models.CharField(max_length=50,default='')

    def __str__(self):
        return self.title
    
