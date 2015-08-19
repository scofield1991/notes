__author__ = 'oleksandr'
from django import  forms
from django.contrib.auth.models import User
from notesapp.models import UserProfile, Note, Label
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator
from captcha.fields import CaptchaField



def validate_username_unique(value):
    exists = User.objects.filter(username=value)
    #user=User.objects.get(pk=request.session['user_id'])
    if exists:
        raise ValidationError("Username %s already exists, must be unique" % value)


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    username= forms.CharField( validators=[validate_username_unique], required=True,
                               widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'required': True, 'class': 'form-control'}), validators=[MaxLengthValidator(16),
                                                                                               MinLengthValidator(6)])
    email=forms.EmailField(widget=forms.EmailInput(attrs={'required': True, 'class': 'form-control'}))

    class Meta:
        model=User
        fields=('first_name', 'last_name', 'username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    birthday=forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'required': True, 'class': 'form-control'}))
    phone_number=forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    #captcha=CaptchaField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))

    class Meta:
        model=UserProfile
        fields=('birthday','phone_number')

class NoteForm(forms.ModelForm):
    note_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    note_body = forms.CharField(widget=forms.Textarea(attrs={ 'class': 'form-control' ,'rows':'5'}))
    user=forms.IntegerField(widget=forms.HiddenInput(), required=False)

    #labels = forms.MultipleChoiceField()
    class Meta:
        model=Note
        fields=('note_name', 'note_body','user', 'labels', 'color','permit')

class LabelForm(forms.ModelForm):
    class Meta:
        fields=('title',)
        model = Label



