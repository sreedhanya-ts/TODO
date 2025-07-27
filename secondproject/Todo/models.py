from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to='profile_pics',blank=True,null=True)
    firstname=models.CharField(max_length=20,blank=True,null=True)
    lastname = models.CharField(max_length=20,blank=True,null=True)
    email=models.CharField(max_length=20,blank=True,null=True)
    phone= models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return self.user.username +" profile"
class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=20,blank=True,null=True)
    deadline=models.DateField(max_length=20,blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    def __str__(self):
        return self.title
    