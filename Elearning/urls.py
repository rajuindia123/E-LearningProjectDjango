"""Elearning1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from userpanel import views as user
from adminpanel import views as adm

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),

    # userpanel urls
    path('',user.home),
    path('mycourse',user.mycourses,name='mycourse'),
    path('login',user.loginuser,name='login'),
    path('signup',user.signupuser,name='signup'),
    path('course/',user.courses,name='course'),
    path('changepass',user.stuchangpass,name='changpass'),
    path('logout',user.logout,name='logout'),

    path('chakout',user.ordersave,name='chakout'),


    path('feedback',user.feedback,name='feddback'),
    path('stuprofile',user.student_profile,name='student_profile'),
    path('cour',user.course_detail,name='course_detail'),
    path('handlerequest',user.handlerequest,name='handlerequest'),
    path('cors/<int:id>/',user.course_detail,name='dcourse'),
    path('watchvideo/<int:id>/',user.watchvideo,name='watchvideo'),

    
    
    # adminpanel urls
    path('admins',adm.deshboard,name='deshboard'),
    path('admincourse',adm.admincourse,name='admincourse'),
    path('addcourse',adm.addcourse,name='addcourse'),
    path('students',adm.student,name='students'),

    path('Contact_Us',adm.Contact,name='Contact_Us'),

    path('addstudents',adm.addstudent,name='addstudents'),
    path('lesson',adm.lesson,name='lesson'),

    path('paymentStatus',adm.paymentStatus,name='paymentStatus'),

    path('feedbacks',adm.feedbacks,name='feed'),
    path('changepassword',adm.changepass,name='changepassword'),

    path('loginadmin',adm.adminLogin,name='loginadmin'),
    path('adminlogout',adm.adminlogout,name='adminlogout'),
    # path('video',adm.addcoursesss,name='video'),
    path('addlesson',adm.addlesson,name='addlesson'),
    path('delete/<int:stu_id>/',adm.delete_stu,name='delstu'),
    path('del/<int:id>/',adm.delete_cors,name='delcourses'),
    path('delleson/<int:id>/',adm.delete_lesson,name='dellesson'),
    path('delfeed/<int:id>/',adm.delete_feedback,name='feeddel'),
    path('<int:stu_id>/',adm.update_stu,name='updatestu'),
    path('cor/<int:id>/',adm.update_cors,name='editcourse'),
    path('editlesson/<int:id>/',adm.update_lesson,name='editlessom'),
    path('delorder/<int:id>/',adm.del_order,name='delorder'),
    path('delcont/<int:id>/',adm.delcont,name='delcont'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

