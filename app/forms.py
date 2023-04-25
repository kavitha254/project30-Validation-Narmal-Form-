from django import forms

def check_for_a(value):
    if value[0]=='a':
         raise forms.ValidationError('name start with a')


def check_for_len(value):
    if len(value)<6:
        raise forms.ValidationError('len is less')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatchar=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        if e!=r:
            raise forms.ValidationError('not matched')

    def clean_botcatchar(self):
        bot=self.cleaned_data['botcatchar']
        if len(bot)>6:
            raise ValidationError('bot')
