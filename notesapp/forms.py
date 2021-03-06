__author__ = 'oleksandr'
from django import  forms
from django.contrib.auth.models import User
from notesapp.models import UserProfile, Note, Label, Category
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator
#from django_select2 import  Select2ChoiceField, Select2MultipleWidget, Select2MultipleChoiceField,Select2Widget
#from captcha.fields import CaptchaField


#Валидация имени пользователя на уникальность
def validate_username_unique(value):
    exists = User.objects.filter(username=value)
    #user=User.objects.get(pk=request.session['user_id'])
    if exists:
        raise ValidationError("Username %s already exists, must be unique" % value)

#Форма регистрации нового пользователя
class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    username= forms.CharField(validators=[validate_username_unique], required=True,
                               widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'required': True, 'class': 'form-control'}), validators=[MaxLengthValidator(16),
                                                                                               MinLengthValidator(6)])
    email=forms.EmailField(widget=forms.EmailInput(attrs={'required': True, 'class': 'form-control'}))

    class Meta:
        model=User
        fields=('first_name', 'last_name', 'username', 'email', 'password')

#Дополнительные сведения в форме регистрации пользователя
class UserProfileForm(forms.ModelForm):
    birthday=forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'required': True, 'class': 'form-control'}))
    phone_number=forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    #captcha=CaptchaField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))

    class Meta:
        model=UserProfile
        fields=('birthday','phone_number')

#Форма для создания заметки
class NoteForm(forms.ModelForm):
    note_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    note_body = forms.CharField(widget=forms.Textarea(attrs={ 'class': 'form-control' ,'rows':'5'}))
    user=forms.IntegerField(widget=forms.HiddenInput(), required=False)
    labels = forms.ModelMultipleChoiceField(Label.objects.all(), widget=forms.SelectMultiple(attrs={ 'class': 'form-control'}))
    category = forms.ModelMultipleChoiceField(Category.objects.all(), widget=forms.SelectMultiple(attrs={ 'class': 'form-control'}))

    #labels = forms.MultipleChoiceField()
    class Meta:
        model=Note
        fields=('note_name', 'note_body','user','category', 'labels', 'color','text','permit')

#Форма для создания ярлыка
class LabelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    class Meta:
        fields=('title',)
        model = Label

#Выбираем все имена и id категории и отображаем их форме создания новой категории
cat_id=[Category.objects.all()[i].id for i in range(len(Category.objects.all()))]
cat_names=[Category.objects.all()[i].name for i in range(len(Category.objects.all()))]
cat_choices=list(zip(cat_id, cat_names))
#cat_choices = list(enumerate([Category.objects.all()[i].name for i in range(len(Category.objects.all()))],1))
cat_choices.append((0,''))


class CategoryForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    parent_category = forms.ChoiceField(choices=cat_choices,  widget=forms.Select(attrs={ 'class': 'form-control'}))
    #parent_category = forms.ChoiceField(choices=cat_choices)




