from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

# 1st(gallery class) 
class Gallery(models.Model):
    title=models.CharField(max_length=200)
    image = CloudinaryField('image')
    description=models.TextField()
    
    
    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

# 2nd(blog class)  
class blog(models.Model):
    blog_photo = CloudinaryField('image', default='image')
    blog_name = models.CharField(max_length=60)
    blog_description = models.TextField(max_length=300, blank=True)       

    def __str__(self):
        return self.blog_name

    def create_blog(self):
        self.save()  

    def save_blog(self):
        self.save()

    def delete_blog(self):
        self.delete()