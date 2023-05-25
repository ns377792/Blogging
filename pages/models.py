from django.db import models

# Create your models here.
     
class Page(models.Model):
    name = models.CharField(max_length=155, unique=True)
    sidebar = models.BooleanField(default=False)
    url = models.CharField(max_length=155)
    content = models.TextField()
    
    def __str__(self):
        return self.name