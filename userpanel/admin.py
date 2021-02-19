from django.contrib import admin
from .models import Signup,CourseOrder

# Register your models here.
@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display=['stu_id','stu_name','stu_email','stu_pass','con_pass','stu_occ','stu_img']

@admin.register(CourseOrder)
class CourseAdmin(admin.ModelAdmin):
    list_display=['id','order_id','student_email','course_id','status','respmsg','amount','order_date']