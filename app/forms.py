from django import forms
from django.core import validators
def check_for_a(value):
    if value[0]=='a':
         raise forms.ValidationError('name start with a')


def check_for_len(value):
    if len(value)<6:
        raise forms.ValidationError('len is less')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,validators.MaxLengthValidator(5)])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatchar=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        if e!=r:
            raise forms.ValidationError('not matched')

    def clean_botcatchar(self):
        bot=self.cleaned_data['botcatchar']
        if len(bot)>0:
            raise ValidationError('bot')
