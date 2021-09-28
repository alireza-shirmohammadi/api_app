from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    phone=models.IntegerField(unique=True,blank=True,null=True)
    email=models.EmailField(unique=True,blank=True,null=True)
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=300,blank=True,null=True)
    last_name=models.CharField(max_length=300,blank=True,null=True)
    img=models.ImageField(upload_to='images',blank=True,null=True)
    creation_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.email
    class Meta :
        db_table = 'user_profile'
