from django.db import models
from adminpanel.models import Addcourse
# Create your models here.
class Signup(models.Model):
    stu_id=models.AutoField(primary_key=True)
    stu_name=models.CharField(max_length=70)
    stu_email=models.EmailField(max_length=70)
    stu_pass=models.CharField(max_length=70)
    con_pass=models.CharField(max_length=70)
    stu_occ=models.CharField(max_length=70,blank=True)
    stu_img=models.ImageField(upload_to='images',default='images/default.png')
       
class CourseOrder(models.Model):
    
    order_id=models.CharField(max_length=70)
    student_email=models.CharField(max_length=70)
    course_id=models.ForeignKey(Addcourse,on_delete=models.CASCADE, null=True, blank=True)
    status=models.CharField(max_length=70)
    respmsg=models.CharField(max_length=70)
    amount=models.CharField(max_length=70)
    order_date=models.DateTimeField()


