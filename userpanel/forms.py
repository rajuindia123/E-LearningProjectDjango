from django import forms
from django.core import validators
from .models import Signup
from django.core.exceptions import ValidationError

from django.core.files.images import get_image_dimensions
import re
class Contact(forms.Form):
    cname=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}),label='Name',validators=[validators.MaxLengthValidator(20)])
    csubject=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}),label='Subject',validators=[validators.MaxLengthValidator(50)])
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),validators=[validators.MaxLengthValidator(30)])
    cmessage=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':3}),label='Message',validators=[validators.MaxLengthValidator(100)]) 
    def clean_cname(self):
        valname = self.cleaned_data["cname"]
        if len(valname)<2 or len(valname)>20 :
            raise forms.ValidationError('Enter Name Between 2 to 20 character!')
        if not re.match(r'^[A-Za-z_ ]+$',valname):
            raise forms.ValidationError("Name should be only Alphabets.")
        return valname
    def clean_csubject(self):
        valname = self.cleaned_data["csubject"]
        if len(valname)<2 or len(valname)>20 :
            raise forms.ValidationError('Enter subject Between 2 to 50 character!')
        if not re.match(r'^[A-Za-z_ ]+$',valname):
            raise forms.ValidationError("subject should be only Alphabets.")
        return valname
    
    def clean_cmessage(self):
        valname = self.cleaned_data["cmessage"]
        if len(valname)<2 or len(valname)>100 :
            raise forms.ValidationError('Enter message Between 2 to 100 character!')
        if not re.match(r'^[A-Za-z0-9_ ]+$',valname):
            raise forms.ValidationError("message should be a combination of Alphabets and Number.")
        return valname





# class Signupform(forms.Form):
#     name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
#     password1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')
#     conpassword2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password(again)')
class Loginform(forms.Form):
    
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','autofocus':'Ture'}))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
class Signupform(forms.ModelForm):
    class Meta:
        model=Signup
        fields=['stu_name','stu_email','stu_pass','con_pass']
        labels={'stu_name':'Enter Full Name:','stu_email':'Enter Email:','stu_pass':'Enter Password:','con_pass':'Password(again) '}
        

        
        widgets={'stu_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name','autofocus':'Ture'}),
        'stu_email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
        'stu_pass':forms.PasswordInput( render_value=True, attrs={'class':'form-control','placeholder':'Enter Password'}),
        'con_pass':forms.PasswordInput( render_value=True, attrs={'class':'form-control ','placeholder':'Password(again)'})
        }
        error_messages={'stu_name':{'required':'Enter Name'},'stu_pass':{'required':'Enter Password'},'stu_email':{'required':'Enter Name'},'con_pass':{'required':'Password(again)'}}
    def clean_stu_name(self):
        valname = self.cleaned_data["stu_name"]
        if len(valname)<2 or len(valname)>30 :
            raise forms.ValidationError('Enter Name Between 2 to 30 character!')
        if not re.match(r'^[A-Za-z_ ]+$',valname):
            raise forms.ValidationError("Name should be only Alphabets.")
        return valname
    def clean_stu_pass(self):
        valpass = self.cleaned_data["stu_pass"]
         
        if len(valpass)<8:
            raise forms.ValidationError('Enter password more then 8 character!')
        if not re.match(r'^[A-Za-z0-9]+$',valpass):
            raise forms.ValidationError("Password should be a combination of Alphabets and Number.")
       
        
        return valpass
    def clean_con_pass(self):
        valpassag = self.cleaned_data["con_pass"]
        if len(valpassag)<8:
            raise forms.ValidationError('Enter password more then 4 char')
        if not re.match(r'^[A-Za-z0-9]+$',valpassag):
            raise forms.ValidationError("Password should be a combination of Alphabets and Number.")
        
        return valpassag
        
        
        
    
    

        
            
        


class studentpro(forms.ModelForm):
    class Meta:
        model=Signup
        fields=['stu_id','stu_email','stu_name','stu_occ','stu_img']
        labels={'stu_id':'Student ID','stu_name':'Student Name','stu_email':'Student Email','stu_occ':'Occupation','stu_img':'Upload Image'}

        
        widgets={'stu_id':forms.TextInput(attrs={'class':'form-control'}),'stu_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Name'}),
        'stu_email':forms.EmailInput(attrs={'class':'form-control','readonly':'Ture'}),
        'stu_occ':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Occupation'}),
        'stu_img':forms.FileInput(attrs={'class':'form-control'})
        }
    def clean_stu_name(self):
        valname = self.cleaned_data["stu_name"]
        if len(valname)<2 or len(valname)>30 :
            raise forms.ValidationError('Enter Name Between 2 to 30 character!')
        if not re.match(r'^[A-Za-z_ ]+$',valname):
            raise forms.ValidationError("Name should be only  Alphabets.")
        return valname

    def clean_stu_occ(self):
        stu_occ = self.cleaned_data["stu_occ"]
        if len(stu_occ)<2 or len(stu_occ)>30 :
            raise forms.ValidationError('Enter occ Between 2 to 30 character!')
        if not re.match(r'^[A-Za-z_ ]+$',stu_occ):
            raise forms.ValidationError("occ should be only  Alphabets.")
        return stu_occ

    def clean_stu_img(self):
        stu_img=self.cleaned_data["stu_img"]
        
        if not stu_img:
            raise forms.ValidationError("No Image Select!")
        else:
            w , h=get_image_dimensions(stu_img)
            if w>=210:
                raise forms.ValidationError("The Image is %i pixel wide. It's supposed to 200px" % w)
            if h>=310:
                raise forms.ValidationError("The Image is %i pixel hight. It's supposed to 300px" % h)
        return stu_img
    
class studentchangpass(forms.ModelForm):
    class Meta:
        model=Signup
        fields=['stu_email','stu_pass','con_pass']
        labels={'stu_pass':'Enter New Password','stu_email':'Student Email','con_pass':'Enter New Password(again)'}

        
        widgets={'stu_email':forms.EmailInput(attrs={'class':'form-control','readonly':'Ture'}),
        'stu_pass':forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password','autofocus':'Ture'}),
        'con_pass':forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password(again)'})
        }
    def clean_stu_pass(self):
        valpass = self.cleaned_data["stu_pass"]
         
        if len(valpass)<8:
            raise forms.ValidationError('Enter password more then 8 character!')
        if not re.match(r'^[A-Za-z0-9]+$',valpass):
            raise forms.ValidationError("Password should be a combination of Alphabets and Number.")
       
        
        return valpass
    def clean_con_pass(self):
        valpassag = self.cleaned_data["con_pass"]
        if len(valpassag)<8:
            raise forms.ValidationError('Enter password more then 4 char')
        if not re.match(r'^[A-Za-z0-9]+$',valpassag):
            raise forms.ValidationError("Password should be a combination of Alphabets and Number.")
        
        return valpassag
    

