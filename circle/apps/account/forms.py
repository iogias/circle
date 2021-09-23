from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# from .models import Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Wallet ID', 'id': 'login-wallet'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Wallet ID', max_length=15,
                               help_text='Required',
                               error_messages={'required': 'Wallet ID YODU'},
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control mb-3',
                                          'placeholder': 'Wallet ID', 'id': 'register-wallet'}
                               ))
    email = forms.EmailField(max_length=100,
                             help_text='Required',
                             error_messages={'required': 'Invalid email'},
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'register-email'}
                             ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Password', 'id': 'register-password'}
    ))
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Repeat Password', 'id': 'register-password2'}
        ))

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count() < 0:
            raise forms.ValidationError('Nomor belum terdaftar di YODU')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email sudah digunakan')
        return email
# class RegistrationForm(forms.ModelForm):
#     user_name = forms.CharField(
#         label='Enter Username', min_length=4, max_length=50, help_text='Required')
#     email = forms.EmailField(max_length=100, help_text='Required', error_messages={
#         'required': 'Invalid email'})
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(
#         label='Repeat password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('username', 'email',)

    # def clean_username(self):
    #     user_name = self.cleaned_data['user_name'].lower()
    #     r = Member.objects.filter(user_name=user_name)
    #     if r.count():
    #         raise forms.ValidationError("Username already exists")
    #     return user_name

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Password tidak cocok')
    #     return cd['password2']

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if AccountUser.objects.filter(email=email).exists():
    #         raise forms.ValidationError(
    #             'Email sudah digunakan')
    #     return email

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['user_name'].widget.attrs.update(
    #         {'class': 'form-control mb-3', 'placeholder': 'Username'})
    #     self.fields['email'].widget.attrs.update(
    #         {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
    #     self.fields['password'].widget.attrs.update(
    #         {'class': 'form-control mb-3', 'placeholder': 'Password'})
    #     self.fields['password2'].widget.attrs.update(
    #         {'class': 'form-control', 'placeholder': 'Repeat Password'})
