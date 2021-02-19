from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .forms import addcourses,addcoursess1,LoginAdmin,ChangePasssword
from .models import Addcourse,Addlesson,Feedback,Contact_Us,Login_Admin
# from django.db.models import Q
# from adminpanel import Signup 
from userpanel.models import Signup,CourseOrder
from userpanel.forms import Signupform
# Create your views here.

def adminLogin(request):
    
    if request.method=='POST':
        fm=LoginAdmin(request.POST)
        if fm.is_valid():
            le=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            stu=Login_Admin.objects.values('email','password').filter(email=le,password=ps)
            exits=stu.exists()
            if exits==True:
                request.session['admin_email']=le
                fm=LoginAdmin()
                return HttpResponseRedirect('/admins')

            else:
                messages.warning(request,'Email and Password wrong!')
    else:
        fm=LoginAdmin()
    return render(request,'admins/adminLogin.html',{'form':fm})



def changepass(request):
    if 'admin_email' in request.session:
        email=request.session['admin_email']
        
        obj=Login_Admin.objects.all().filter(email=email)
        if request.method=='POST':
            pi=Login_Admin.objects.get(email=email)
            form=ChangePasssword(request.POST or None,instance=pi or None)
            if form.is_valid():
                ps=form.cleaned_data['password']
                co=form.cleaned_data['email']
                
                form.save()
                form=ChangePasssword(instance=pi)
                messages.success(request,'Update in Successfully!!')
                
            
                    
        else:
                pi=Login_Admin.objects.get(email=email)
                form=ChangePasssword(instance=pi)
        return render(request,'admins/changepass.html',{'change':'active','form':form,'obj':obj})
    else:
        return HttpResponseRedirect('/loginadmin')




def deshboard(request):
    if 'admin_email' in request.session:
        stu_cont=Signup.objects.all().count()
        cour=Addcourse.objects.all().count()
        con=CourseOrder.objects.all()
        orde_count=CourseOrder.objects.all().count()
        # print(orde_count)
        context={'home':'active','order':con,'stu_count':stu_cont,'cour_count':cour,'order_count':orde_count}
        return render(request,'admins/index.html',context)
    else:
        return HttpResponseRedirect('/loginadmin')


def Contact(request):
    if 'admin_email' in request.session:
        cor=Contact_Us.objects.all()
        return render(request,'admins/contact_Us.html',{'cor':cor})
    else:
        return HttpResponseRedirect('/loginadmin')

def delcont(request, id):
    if 'admin_email' in request.session:
        if request.method == 'POST':
            pi= Contact_Us.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/Contact_Us')
    else:
        return HttpResponseRedirect('/loginadmin')

        
def admincourse(request):
    if 'admin_email' in request.session:
        cor=Addcourse.objects.all()
        return render(request,'admins/course.html',{'cor':cor,'cors':'active'})
    else:
        return HttpResponseRedirect('/loginadmin')
    
    
def addcourse(request):
    if 'admin_email' in request.session:
        if request.method=='POST':
            fm=addcourses(request.POST,request.FILES)
            if fm.is_valid():
                nm=fm.cleaned_data['name']
                des=fm.cleaned_data['description']
                au=fm.cleaned_data['author']
                dur=fm.cleaned_data['duration']
                o_p=fm.cleaned_data['o_price']
                s_p=fm.cleaned_data['s_price']
                img=fm.cleaned_data['img']
                res=Addcourse(name=nm,description=des,author=au,duration=dur,o_price=o_p,s_price=s_p,img=img)
                res.save()
                fm=addcourses()
                messages.success(request,'Course Add  in Successfully!!')
        else:
            fm=addcourses()
        return render(request,'admins/addcourse.html',{'form':fm,'cors':'active'})
    else:
        return HttpResponseRedirect('/loginadmin')
    
def student(request):
    if 'admin_email' in request.session:
        stus=Signup.objects.all()
    
        return render(request,'admins/students.html',{'stus':stus,'stu':'active'})
    else:
        return HttpResponseRedirect('/loginadmin')
    
def addstudent(request):
    if 'admin_email' in request.session:
        if request.method=='POST':
            fms=Signupform(request.POST)
            if fms.is_valid():
                nm=fms.cleaned_data['name']
                em=fms.cleaned_data['email']
                pw=fms.cleaned_data['password1']
                co_pw=fms.cleaned_data['conpassword2']
                # occ_name=fms.cleaned_data['occ_name']
                if pw==co_pw:
                    # stu=Signup.objects.filter(stu_email=em)
                    stu=Signup.objects.values('stu_email').filter(stu_email=em)

                    exits=stu.exists()
                    if exits==True:
                        messages.warning(request,'Email Id Already exists !')
                    else:
                        res=Signup(stu_name=nm,stu_email=em,stu_pass=pw,con_pass=co_pw)
                        res.save()
                        messages.success(request,'Register in Successfully!!')
                        

                        fms=Signupform()
                else:
                    messages.warning(request,'password and confirm does  not match !')
        else:
            fms=Signupform()
        return render(request,'admins/addstudent.html',{'stu':'active','form':fms })
    else:
        return HttpResponseRedirect('/loginadmin')
#delete student
def delete_stu(request, stu_id):
    if 'admin_email' in request.session:
        if request.method == 'POST':
            pi= Signup.objects.get(pk=stu_id)
            pi.delete()
            return HttpResponseRedirect('/students')
    else:
        return HttpResponseRedirect('/loginadmin')
        
#delete course
def delete_cors(request, id):
    if 'admin_email' in request.session:
        if request.method == 'POST':
            pis= Addcourse.objects.get(pk=id)
            pis.delete()
            return HttpResponseRedirect('/admincourse')
    else:
        return HttpResponseRedirect('/loginadmin')
        
#Updatae Student
def update_stu(request, stu_id):
    if 'admin_email' in request.session:
        if request.method=='POST':
            pi=Signup.objects.get(pk=stu_id)
            form=Signupform(request.POST,instance=pi)
            if form.is_valid():
                # nm=form.cleaned_data['stu_name']
                # em=form.cleaned_data['stu_email']
                pw=form.cleaned_data['stu_pass']
                co_pw=form.cleaned_data['con_pass']
                # occ_name=fms.cleaned_data['occ_name']
                if pw==co_pw:
                    # stu=Signup.objects.filter(stu_email=em)
                    # stu=Signup.objects.values('stu_email').filter(stu_email=em)

                    # exits=stu.exists()
                    # if exits==True:
                    #     messages.warning(request,'Email Id Already exists !')
                    # else:
                    # res=Signup(stu_name=nm,stu_email=em,stu_pass=pw,con_pass=co_pw)
                    form.save()
                    messages.success(request,'Update in Successfully!!')
                        

                    form=Signupform(instance=pi)
                else:
                    messages.warning(request,'password and confirm does  not match !')
        else:
            pi=Signup.objects.get(pk=stu_id)
            form=Signupform(instance=pi)
        return render (request,'admins/updatestudent.html',{'form':form,'stu':'active'})
    else:
        return HttpResponseRedirect('/loginadmin')



#Updatae course
def update_cors(request,id):
    if 'admin_email' in request.session:
        if request.method=='POST':
            pi=Addcourse.objects.get(pk=id)
            form=addcourses(request.POST,instance=pi)
            if form.is_valid():
                
                form.save()
                messages.success(request,'Update in Successfully!!')
                form=addcourses(instance=pi)
                
        else:
            pi=Addcourse.objects.get(pk=id)
            form=addcourses(instance=pi)
        return render (request,'admins/editcourse.html',{'form':form,'cors':'active'})
    else:
        return HttpResponseRedirect('/loginadmin')



def lesson(request):
    if 'admin_email' in request.session:
        # if request.method=='POST':
        if request.method=='POST':
            given_name=request.POST['srh']
            
            if given_name:
                
                
                ser_course=Addcourse.objects.filter(id=given_name) 
                
                if ser_course:
                    for co in ser_course:
                        c_id=co.id
                        c_name=co.name
                        request.session['course_id']=c_id
                        request.session['course_name']=c_name
                    cid=request.session['course_id']
                    lesson=Addlesson.objects.all().filter(course_id=cid)  
                    return render(request,'admins/lesson.html',{'lesson':'active','cor':ser_course,'les':lesson})
                else:
                    messages.warning(request,'No Result Found!')
                    
            else:
                return HttpResponseRedirect('/lesson')
        return render(request,'admins/lesson.html',{'lesson':'active'})
    else:
        return HttpResponseRedirect('/loginadmin')
        
# def addlesson(request):
#     if request.method=='POST':
        
#             # add=Addlesson
#         add_id=request.POST['course_id']
#         add_name=request.POST['name']
#         add_course_name=request.POST['course_name']
#         add_desc=request.POST['desc']
#         add_video_link=request.POST['video_link']
#         # add_video_link=request.FILES['video_link']
#         res=Addlesson(name=add_name,desc=add_desc,course_name=add_course_name,course_id=add_id,video_link=add_video_link)
#         res.save()
#         return HttpResponseRedirect('/')
#     else:
#         course_id=request.session['course_id']
#         course_name=request.session['course_name']
#         return render(request,'admins/addlesson.html',{'cid':course_id,'cname':course_name})
def addlesson(request):
    if 'admin_email' in request.session:
        if request.method=='POST':
            fm=addcoursess1(request.POST,request.FILES)
            if fm.is_valid():
                nm=fm.cleaned_data['name']
                des=fm.cleaned_data['desc']
                # cid=fm.cleaned_data['course_id']
                cid=request.session['course_id']
                dur=request.session['course_name']
                # dur=fm.cleaned_data['course_name']
                o_p=fm.cleaned_data['video_link']
                
                res=Addlesson(name=nm,desc=des,course_id=cid,course_name=dur,video_link=o_p)
                res.save()
                fm=addcoursess1()
                messages.success(request,'Lesson Add  in Successfully!!')
        else:
            fm=addcoursess1()
        return render(request,'admins/addlesson.html',{'form':fm,'lesson':'active'})
    else:
        return HttpResponseRedirect('/loginadmin')
#delete lesson
def delete_lesson(request, id):
    if 'admin_email' in request.session:
        if request.method == 'POST':
            pis= Addlesson.objects.get(pk=id)
            pis.delete()
            return HttpResponseRedirect('/lesson')
    else:
        return HttpResponseRedirect('/loginadmin')
#Update lesson
def update_lesson(request,id):
    if 'admin_email' in request.session:
        if request.method=='POST':
            pi=Addlesson.objects.get(pk=id)
            form=addcoursess1(request.POST,instance=pi)
            if form.is_valid():
                
                form.save()
                messages.success(request,'Update in Successfully!!')
                form=addcoursess1(instance=pi)
                
        else:
            pi=Addlesson.objects.get(pk=id)
            form=addcoursess1(instance=pi)
        # pii=Addlesson.objects.filter(id=id)
        return render (request,'admins/editlesson.html',{'form':form,'lesson':'active'})
    else:
        return HttpResponseRedirect('/loginadmin')

def feedbacks(request):
    if 'admin_email' in request.session:
        pi=Feedback.objects.all()
        return render (request,'admins/feedback.html',{'cor':pi,'feed':'active'})
    else:
        return HttpResponseRedirect('/loginadmin')

#delete FeddBach
def delete_feedback(request, id):
    if 'admin_email' in request.session:
        if request.method == 'POST':
            pis=Feedback.objects.get(pk=id)
            pis.delete()
            return HttpResponseRedirect('/feedbacks')
    else:
        return HttpResponseRedirect('/loginadmin')
def del_order(request, id):
    if 'admin_email' in request.session:
        if request.method=='POST':
            delorder=CourseOrder.objects.get(pk=id)
            delorder.delete()
            return HttpResponseRedirect('/admins')
    else:
        return HttpResponseRedirect('/loginadmin')

def paymentStatus(request):
    if 'admin_email' in request.session:
        if request.method=='POST':
            given_name=request.POST['srh']
            
            if given_name:
                
                
                ser_course=CourseOrder.objects.filter(order_id=given_name) 
                
                if ser_course:
                    # for co in ser_course:
                    #     c_id=co.id
                        
                    #     request.session['order_id']=c_id
                        
                    # cid=request.session['order_id']
                    # order=CourseOrder.objects.all().filter(order_id=cid)  
                    return render(request,'admins/paymentStatus.html',{'pay':'active','les':ser_course})
                else:
                    messages.warning(request,'No Result Found!')
                    
            else:
                return HttpResponseRedirect('/paymentStatus')

        return render(request,'admins/paymentStatus.html',{'pay':'active'})
    else:
        return HttpResponseRedirect('/loginadmin')


def adminlogout(request):
    if 'admin_email' in request.session:
        del request.session['admin_email']
        return HttpResponseRedirect('/loginadmin')
