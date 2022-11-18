from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SignUp



class SingUpModelForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username', 
            'type': 'text',
            'class': 'form-input', 
            'maxlength': '16', 
            'minlength': '6'
        })
        self.fields["email"].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email', 
            'type': 'email',
            'class': 'form-input', 
            'maxlength': '32', 
            'minlength': '6'
        })
        self.fields["password1"].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1', 
            'type': 'password',
            'class': 'form-input', 
            'maxlength': '16', 
            'minlength': '6'
        })
        self.fields["password2"].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2', 
            'type': 'password',
            'class': 'form-input', 
            'maxlength': '16', 
            'minlength': '6'
        })
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')



    class Meta:
        model = SignUp
        fields = ['username', 'email', 'password1', 'password2']
        