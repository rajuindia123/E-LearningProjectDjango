from django.contrib import admin
from .models import Addcourse,Addlesson,Feedback,Contact_Us,Login_Admin
# Register your models here.
@admin.register(Addcourse)
class AddAdmin(admin.ModelAdmin):
    list_display=['id','name','description','author','duration','o_price','img','s_price']


@admin.register(Addlesson)
class Addles(admin.ModelAdmin):
    list_display=['id','name','desc','course_id','course_name','video_link']
@admin.register(Feedback)
class Addless(admin.ModelAdmin):
    list_display=['id','contant','stu_id']

@admin.register(Contact_Us)
class AddContact_Us(admin.ModelAdmin):
    list_display=['id','name','subject','email','message']

@admin.register(Login_Admin)
class AddLoginAdmin(admin.ModelAdmin):
    list_display=['id','email','password']