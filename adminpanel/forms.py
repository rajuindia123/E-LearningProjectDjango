from django import forms
from .models import Addcourse,Addlesson,Feedback,Login_Admin
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.files.images import get_image_dimensions
import re


class LoginAdmin(forms.Form):
    
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','autofocus':'Ture'}))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control'}))

class addcourses(forms.ModelForm):
    class Meta:
        model=Addcourse
        fields='__all__'
        labels={'name':'Course Name:','description':'Course Description:','author':'Author:','duration':'Duration:','o_price':'Course Original Price:','s_price':'Course Selling Price:','img':'Course Image:'}

        widgets={'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Course Name','autofocus':'Ture'}),
        'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Course Description','rows':2}),
        'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Author Name'}),
        'duration':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Duration'}),
        'o_price':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Course Original Price','onkeypress':'isInputNumber(event)'}),
        's_price':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Course Selling Price','onkeypress':'isInputNumber(event)'}),
        'img':forms.FileInput(attrs={'class':'form-control-file form-control'})
        }

        error_messages={'name':{'required':'Enter Name'},'description':{'required':'Enter Description'},'author':{'required':'Enter Author Name'},'duration':{'required':'Enter Duration'},'o_price':{'required':'Enter Course Original Price'},'s_price':{'required':'Enter Course Selling Price'},'img':{'required':'Upload Image'}}


    # def clean_name(self):
    #     valname = self.cleaned_data["name"]
    #     if len(valname)<2 or len(valname)>30 :
    #         raise forms.ValidationError('Enter Name Between 2 to 30 character!')
    #     if not re.match(r'^[A-Za-z0-9_ ]+$',valname):
    #         raise forms.ValidationError("Name should be a combination of Alphabets and Number.")
    #     return valname
    
    # def clean_description(self):
    #     valname = self.cleaned_data["description"]
    #     if len(valname)<10 or len(valname)>300 :
    #         raise forms.ValidationError('Enter Description Between 10 to 300 character!')
    #     if not re.match(r'^[A-Za-z0-9_ ]+$',valname):
    #         raise forms.ValidationError("Description should be a combination of Alphabets and Number.")
    #     return valname
    # def clean_author(self):
    #     valname = self.cleaned_data["author"]
    #     if len(valname)<2 or len(valname)>30 :
    #         raise forms.ValidationError('Enter Author Name Between 2 to 30 character!')
    #     if not re.match(r'^[A-Za-z0-9_ ]+$',valname):
    #         raise forms.ValidationError("Author Name should be a combination of Alphabets and Number.")
    #     return valname
    
    # def clean_duration(self):
    #     valname = self.cleaned_data["duration"]
    #     if len(valname)<2 or len(valname)>20 :
    #         raise forms.ValidationError('Enter Duration Between 2 to 20 character!')
        
    #     return valname


    # def clean_img(self):
    #     img=self.cleaned_data.get("img")

        
    #     if not img:
    #         raise forms.ValidationError("No Image Select!")
    #     else:
    #         w,h=get_image_dimensions(img)
    #         if w>=900:
    #             raise forms.ValidationError("The Image is %i pixel wide. It's supposed to 200px" % w)
    #         if h>=1000:
    #             raise forms.ValidationError("The Image is %i pixel hight. It's supposed to 200px" % h)
    #     return img
class addcoursess1(forms.ModelForm):
    class Meta:
        model=Addlesson
        fields=['name','desc','video_link']
        labels={'name':'Enter Lesson Name:','desc':'Enter Description','video_link':'Upload Video Link'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Lesson Name:','autofocus':'Ture'}),
        'desc':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Lesson Description','rows':3}),'video_link':forms.FileInput(attrs={'class':'form-control form-control-file','placeholder':'Uplode Video Link:'})}


        error_messages={'name':{'required':'Enter Name'},'desc':{'required':'Enter Description'},'video_link':{'required':'Upload Video Link'}}

    # def clean_name(self):
    #     valname = self.cleaned_data["name"]
    #     if len(valname)<2 or len(valname)>30 :
    #         raise forms.ValidationError('Enter Name Between 2 to 30 character!')
    #     if not re.match(r'^[A-Za-z0-9_ ]+$',valname):
    #         raise forms.ValidationError("Name should be a combination of Alphabets and Number.")
    #     return valname

    # def clean_desc(self):
    #     valname = self.cleaned_data["desc"]
    #     if len(valname)<2 or len(valname)>200 :
    #         raise forms.ValidationError('Enter Description Between 2 to 200 character!')
    #     if not re.match(r'^[A-Za-z0-9_ ]+$',valname):
    #         raise forms.ValidationError("Description should be a combination of Alphabets and Number.")
    #     return valname


    
class Stufeed(forms.ModelForm):
    email=forms.EmailField(label='Student Email ID',widget=forms.EmailInput(attrs={'class':'form-control','readonly':'Ture'}))
    class Meta:
        model=Feedback
        fields=['id','contant']
        labels={'contant':'Write Feedback'}
        widgets={'contant':forms.Textarea(attrs={'class':'form-control','placeholder':'Write Feedback:','rows':3,'autofocus':'Ture'})}
        error_messages={'contant':{'required':'Enter Feedback'}}
    def clean_contant(self):
        valname = self.cleaned_data["contant"]
        if len(valname)<5 or len(valname)>100 :
            raise forms.ValidationError('Enter Feedback Between 5 to 100 character!')
        if not re.match(r'^[A-Za-z0-9_ ]+$',valname):
            raise forms.ValidationError("Feedback should be a combination of Alphabets and Number.")
        return valname


class ChangePasssword(forms.ModelForm):
    class Meta:
        model=Login_Admin
        fields=['email','password']
        labels={'password':'Enter New Password','email':'Admin  Email Id'}

        
        widgets={'email':forms.EmailInput(attrs={'class':'form-control','readonly':'Ture'}),
        'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password','autofocus':'Ture'})
        
        }
    def clean_password(self):
        valpass = self.cleaned_data["password"]
         
        if len(valpass)<8:
            raise forms.ValidationError('Enter password more then 8 character!')
        if not re.match(r'^[A-Za-z0-9]+$',valpass):
            raise forms.ValidationError("Password should be a combination of Alphabets and Number.")
       
        
        return valpass
    # def clean_con_pass(self):
    #     valpassag = self.cleaned_data["con_pass"]
    #     if len(valpassag)<8:
    #         raise forms.ValidationError('Enter password more then 4 char')
    #     if not re.match(r'^[A-Za-z0-9]+$',valpassag):
    #         raise forms.ValidationError("Password should be a combination of Alphabets and Number.")
        
    #     return valpassag
    

