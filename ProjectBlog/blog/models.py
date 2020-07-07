from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    overview = models.CharField(max_length=500)
    default = RichTextField()
    postimage = models.ImageField()
    tag = models.ManyToManyField(Category, null=True)
    timestamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.sno) + "--->"+self.title 

class Comment(models.Model):
    coms = models.TextField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    postby = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)    
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='parentcom')
    commentBy = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.coms

class Signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    pass1 = models.CharField(max_length=100)
    pass2 = models.CharField(max_length=100)

    def __str__(self):
        return self.username + '--->' +self.email
    