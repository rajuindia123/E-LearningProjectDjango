from django.db import models
# from userpanel.models import CourseOrder
# from userpanel.models import Signup

# Create your models here.
class Addcourse(models.Model):
    name=models.CharField(max_length=70)
    description=models.TextField(max_length=220)
    author=models.CharField(max_length=70)
    duration=models.CharField(max_length=70)
    o_price=models.CharField(max_length=70)
    s_price=models.CharField(max_length=70)
    img=models.ImageField(upload_to='images')
    


class Addlesson(models.Model):
    name=models.CharField(max_length=70)
    desc=models.TextField(max_length=70)
   
    course_id=models.CharField(max_length=70)
    course_name=models.CharField(max_length=70)
    video_link=models.FileField(upload_to='video/')
    
class Feedback(models.Model):
    contant=models.TextField(max_length=255)
    stu_id=models.CharField(max_length=70)
    # stu_id1=models.ForeignKey(Singup)
    
     
class Contact_Us(models.Model):
    name=models.CharField(max_length=70)
    subject=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField(max_length=300)


class Login_Admin(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=50)
    
    