from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField



# Create your models here.


class Blog(models.Model):
    blog_photo = CloudinaryField("image", default="image")
    blog_name = models.CharField(max_length=60)
    blog_intro = models.CharField(max_length=60 ,null=True)
    blog_description = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.blog_name

    class Meta:
        ordering = ["-id"]

    def create_blog(self):
        self.save()

    def save_blog(self):
        self.save()

    def delete_blog(self):
        self.delete()

    def all_blogs(cls):
        blogs = cls.objects.all()
        return blogs

class Gallery(models.Model):
    galleryimage = models.ImageField(
        "Gallery Image", null=False, blank=False, upload_to="uploads/"
    )
    image_title = models.CharField(max_length=200, default='DARAJA_CIF')
    image_description = HTMLField()

    def __str__(self):
        return self.image_title

    class Meta:
        ordering = ["-id"]

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


class Projects(models.Model):
    proj_image = models.ImageField(
        "Project Image", null=False, blank=False, upload_to="projects/"
    )
    proj_title = models.CharField(max_length=200)
    proj_description = HTMLField()
    project_date = models.DateField()

    def __str__(self):
        return self.proj_title

    class Meta:
        ordering = ["-id"]
    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
    
class Contact(models.Model):
    fullname = models.CharField("Full Name", max_length=500)
    email = models.EmailField('Email', max_length=255)
    # pnumber = models.IntegerField()
    message = models.TextField()
    

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-id"]
        
    def save_contact(self):
        self.save()

    def delete_contact(self):
        self.delete()

     