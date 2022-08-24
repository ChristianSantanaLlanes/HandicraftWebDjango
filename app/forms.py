from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'tt-input','placeholder':'Direccion de correo'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'tt-input','placeholder':'Contraseña'}))