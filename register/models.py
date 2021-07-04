from django.contrib.auth.models import User
from django.db import  models
import datetime
from django.db.models.fields.related import OneToOneField
from django.db.models.signals import post_save


# Create your models here.

class BlogOrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-blogtime')




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    userImage = models.ImageField(upload_to="images/",null=True,blank=True,default="default_profile.jpg")
    bio = models.CharField(max_length=150, null=True,blank=True)

    def __str__(self):
        return self.user.username

class ProfileGallery(models.Model):
    userInfo = models.ForeignKey(User, on_delete=models.CASCADE)
    userGallery = models.ImageField(upload_to="profile/",blank=True,null=True)

    def __str__(self):
        return self.userInfo.username

class Blog(models.Model):
    blogtitle = models.CharField(max_length=60)
    blogpost = models.TextField()
    blogtime = models.DateTimeField(auto_now_add=True)
    blog_user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_author = models.CharField(max_length=60,default=User)
    objects = models.Manager()
    date_objects = BlogOrderManager()

    def __str__(self):
        return self.blogtitle + " " + self.blog_author



class Contact(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    messages = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name



def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_profile, sender=User)

def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.userprofile.save()
post_save.connect(create_profile, sender=User)

