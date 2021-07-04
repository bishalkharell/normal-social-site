from django.contrib import admin
from .models import Blog, UserProfile,ProfileGallery,Contact
# Register your models here.

admin.site.register((Blog,UserProfile,ProfileGallery,Contact))