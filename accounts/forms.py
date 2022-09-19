from django import forms

class UserRegistrationForm(forms.Form):
    username= forms.CharField(label='نام کاربری')
    mobile_phone = forms.CharField(label='شماره موبایل')
    gender = forms.CharField(label='جنسیت')
    first_name = forms.CharField(label='نام')
    last_name = forms.CharField(label='نام خانوادگی')
    password = forms.CharField(label='گذرواژه')
    
class UserloginForm(forms.Form):
    mobile_phone= forms.CharField(label='شماره موبایل')
    password= forms.CharField(label='رمز عبور')