from django import forms
from django.core import  validators
from firstapp.models import Users, UserProfileInfor
from django.contrib.auth.models import User

def check(value):
    if value[0].lower() != 'b':
        raise forms.ValidationError("Name must start with 'B'")

class FormName(forms.Form):
    name = forms.CharField(label="Your Name",validators=[check])
    email = forms.EmailField()
    verify_email=forms.EmailField(label="Re enter mail")
    text = forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        all_clean = super().clean()
        
        e1 = all_clean['email']
        v1 = all_clean['verify_email']
        if e1 != v1:
            raise forms.ValidationError("Emails must match")


class NewUser(forms.ModelForm):
     class Meta:
        model = Users
        fields = '__all__'
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoform(forms.ModelForm):
    class Meta:
        model=UserProfileInfor
        fields=('portfolio_site','profile_pic')