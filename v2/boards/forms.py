from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class InputForm(forms.Form):
    nombres= forms.CharField(max_length=200)
    apellidos= forms.CharField(max_length=200)
    prioridad= forms.IntegerField(min_value=1, max_value=3)
    contrasenna = forms.CharField(widget=forms.PasswordInput)
    habilitado = forms.BooleanField()
    

class WidgetForm(forms.Form):
    nombres= forms.CharField(max_length=200, widget=forms.Textarea)
    apellidos= forms.CharField(max_length=200)
    prioridad= forms.IntegerField(min_value=1, max_value=3)
    contrasenna = forms.CharField(widget=forms.PasswordInput)
    habilitado = forms.BooleanField()
    fecha = forms.DateField(widget=forms.SelectDateWidget)
    
class BoardsForm(forms.Form):
    class Meta:
        model = BoardsModel
        fields = "__all__"
        exclude = ["modificado"]    
    
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')
        
        
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

