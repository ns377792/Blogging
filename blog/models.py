from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    featured = models.BooleanField()
    def __str__(self):
            return self.name

class blogpost(models.Model):
    heading = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    description = models.CharField(max_length=303)
    slug = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured_post = models.BooleanField()
    featured_image = models.ImageField(upload_to="blog/featrued_image/")
    content = models.TextField()
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    similar_posts = models.ManyToManyField('self', null=True, blank=True)

    def __str__(self):
        return self.name+" - "+str(self.date)

class Comment(models.Model):
    user = models.CharField(max_length=50)
    blog_post = models.ForeignKey(blogpost, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return str(self.user)+" - "+self.comment

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    