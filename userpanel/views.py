from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib import messages
from .forms import Contact,Signupform,Loginform,studentpro,studentchangpass
from .models import Signup,CourseOrder

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from adminpanel.models import Feedback,Addcourse,Addlesson,Contact_Us
from adminpanel.forms import Stufeed
from .import Checksum
import string
import random
from django.template import RequestContext



MERCHANT_KEY = 'white your merchant Key'
def home(request):
    if request.method=='POST':
        fm=Contact(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['cname']
            sb=fm.cleaned_data['csubject']
            em=fm.cleaned_data['email']
            msg=fm.cleaned_data['cmessage']
            res=Contact_Us(name=name,email=em,subject=sb,message=msg)
            res.save()
            messages.success(request,'Contact message send in Successfully!!')
            fm=Contact()
    else:
        fm=Contact()



    pi=Addcourse.objects.all()[:8]
    feed=Feedback.objects.all()
    # for fe in feed:
    #     print(fe.stu_id)

    return render(request,'users/home.html',{'form':fm,'cor':pi,'hom':'active','feed':feed})


def loginuser(request):
    if request.method=='POST':
        fm=Loginform(request.POST)
        if fm.is_valid():
            le=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            stu=Signup.objects.values('stu_email','stu_pass').filter(stu_email=le,stu_pass=ps)
            exits=stu.exists()
            if exits==True:
                request.session['stu_email']=le
                fm=Loginform()
                return HttpResponseRedirect('/')

            else:
                messages.warning(request,'Email and Password wrong')
    else:
        fm=Loginform()
    return render(request,'users/login.html',{'form':fm})

def signupuser(request):
    if request.method=='POST':
        fm=Signupform(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['stu_name']
            em=fm.cleaned_data['stu_email']
            pw=fm.cleaned_data['stu_pass']
            co_pw=fm.cleaned_data['con_pass']
            

            if pw==co_pw:
                # stu=Signup.objects.filter(stu_email=em)
                stu=Signup.objects.values('stu_email').filter(stu_email=em)

                exits=stu.exists()
                if exits==True:
                    messages.warning(request,'Email Id Already exists !')
                else:
                   
                    request.session['stu_name']=nm
                    res=Signup(stu_name=nm,stu_email=em,stu_pass=pw,con_pass=co_pw)
                    res.save()
                    messages.success(request,'Register in Successfully!!')
                    messages.info(request,'Now you con Login !!')

                    fm=Signupform()
            else:
                messages.warning(request,'password and confirm does  not match !')
    else:
        fm=Signupform()
    
    return render(request,'users/signup.html',{'form':fm})
def courses(request):
    
    pi=Addcourse.objects.all()
    
    return render(request,'users/course.html',{'cor':pi,'coc':'active'})

# def student_profile(request):
#     email=request.session['stu_email']
#     if request.method=='POST':
#         fm=studentpro(request.POST,request.FILES)
#         # if fm.is_valid():
#         nm=request.POST['stu_name']
#         # pic=request.POST['stu_img']
        
#         occ=request.POST['stu_occ']
#         if fm.is_valid():
#             pic=fm.cleaned_data['stu_img']
#             pi=Signup.objects.filter(stu_email=email).update(stu_name=nm,stu_img=pic,stu_occ=occ)
            
#     else:
#         # pass
#         pi=Signup.objects.filter(stu_email=email)
#         for cor in pi:
#             init_dict={'stu_email':cor.stu_email,'stu_name':cor.stu_name,'stu_occ':cor.stu_occ}
#         fm=studentpro(initial=init_dict)
#     return render(request,'users/studentprofile.html',{'pro':'active','form':fm})



def feedback(request):
    if 'stu_email' in request.session:
        email=request.session['stu_email']
    
    
        obj=Signup.objects.all().filter(stu_email=email)
        if request.method=='POST':
            fm=Stufeed(request.POST or None)
            if fm.is_valid():
                em=fm.cleaned_data['email']
                fd=fm.cleaned_data['contant']
                res=Feedback(contant=fd,stu_id=em)
                res.save()
                messages.success(request,'Feedback Send in Successfully!!')
                fm=Stufeed(initial={'email':email})


        else:
            fm=Stufeed(initial={'email':email})
        return render(request,'users/feedback.html',{'feed':'active','form':fm,'email':email,'obj':obj})
    else:
        return HttpResponseRedirect('/')
#............................................................
def student_profile(request):
    if 'stu_email' in request.session:

        email=request.session['stu_email']
        obj=Signup.objects.all().filter(stu_email=email)
        if request.method=='POST':
            pi=Signup.objects.get(stu_email=email)
            form=studentpro(request.POST or None , request.FILES or None,instance=pi or None)
            if form.is_valid():
                
                form.save()
                messages.success(request,'Update in Successfully!!')
                form=studentpro(instance=pi)
                
        else:
            pi=Signup.objects.get(stu_email=email)
            form=studentpro(instance=pi)
        
        return render(request,'users/studentprofile.html',{'pro':'active','form':form,'obj':obj})
    else:
        return HttpResponseRedirect('/')
def logout(request):
    if 'stu_email' in request.session:
        del request.session['stu_email']
        return HttpResponseRedirect('/')


def stuchangpass(request):
    if 'stu_email' in request.session:
        email=request.session['stu_email']
    
        obj=Signup.objects.all().filter(stu_email=email)
        if request.method=='POST':
            pi=Signup.objects.get(stu_email=email)
            form=studentchangpass(request.POST or None,instance=pi or None)
            if form.is_valid():
                ps=form.cleaned_data['stu_pass']
                co=form.cleaned_data['con_pass']
                if ps==co:
                    form.save()
                    form=studentchangpass(instance=pi)
                    messages.success(request,'Update in Successfully!!')
                else:
                    form=studentchangpass(instance=pi)
                    messages.warning(request,'password and confirm does  not match !')
        
                
        else:
            pi=Signup.objects.get(stu_email=email)
            form=studentchangpass(instance=pi)
        return render(request,'users/stuchangepass.html',{'chan':'active','form':form,'obj':obj})
    else:
        return HttpResponseRedirect('/')

def mycourses(request):
    if 'stu_email' in request.session:
        email=request.session['stu_email']

        obj=Signup.objects.all().filter(stu_email=email)

        q1=CourseOrder.objects.values_list('course_id','course_id__name','course_id__description','course_id__author','course_id__duration','course_id__s_price',named=True).filter(student_email=email)
        # for i in q1:
        #     print("name:",i.course_id__name)
        #     print("description:",i.course_id__description)
        #     print("name author:",i.course_id__author)
        #     print("name duration:",i.course_id__duration)
        #     print("name:s_price",i.course_id__s_price)
        #     print("name:s_price",i.course_id__img)
        #     print("------------")
                
       
        return render(request,'users/mycourse.html',{'mycor':'active','obj':obj,'q1':q1})
    else:
        return HttpResponseRedirect('/')



def course_detail(request,id):
    
    pi=Addcourse.objects.all().filter(id=id)
    ls=Addlesson.objects.all().filter(course_id=id)
    for cors in ls:
        cid=cors.course_id
    # print("CourseId:",cid)
    if cid:
        request.session['cou_id']=cid
    N=10
    res=''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    if request.method=='POST':
        for pp in pi:
            cc=pp.s_price
            
        if 'stu_email' in request.session:
            email=request.session['stu_email']
            param_dict = {

                'MID': 'CtLymr21190006307754',
                'ORDER_ID': str(res),
                'TXN_AMOUNT': cc,
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest',

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        else:
            return HttpResponseRedirect('/login')
        return render(request, 'users/paytm.html', {'param_dict': param_dict})
    # print("hekkio",cc)
    
    # print("The Generated random string:" + str(res))
    # em=request.session['stu_email']
    # cid=request.session['course_id']
    
    return render(request,'users/course_detail.html',{'cor':pi,'less':ls})


@csrf_exempt
def handlerequest(request):
    
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            
            

        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'users/paymentstatus.html', {'response': response_dict})


def ordersave(request):
   
    if request.method=='POST':
        email=request.session['stu_email']
        cid=request.session['cou_id']
        o_id=request.POST['order_id']
        am=request.POST['amount']
        date=request.POST['date']
        status=request.POST['status']
        resmsg=request.POST['respmsg']
        res=CourseOrder(student_email=email,status=status,respmsg=resmsg,order_date=date,amount=am,order_id=o_id)
        res.save()
        #course_id
        print(res)
        print(email)
        print(cid)
        print(o_id)
        print(am)
        print(date)
        print(resmsg)
        print(status)
    return render(request,'users/mycourse.html')
    


def watchvideo(request,id):
    if 'stu_email' in request.session:
        less=Addlesson.objects.all().filter(course_id=id)
        return render(request, 'users/watchcourse.html',{'less':less})
    else:
        return HttpResponseRedirect('/')
    