from django import forms
from django.core import validators  #for implicit validators
def start_with_p(value):
    if value[0]!='p':
        raise forms.ValidationError("Name should start with p")


class feedbackform(forms.Form):
    name=forms.CharField(validators=[start_with_p])
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Re enter password',widget=forms.PasswordInput)
    age=forms.IntegerField()
    email=forms.EmailField()  #[len(a)-9:]
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MinLengthValidator(10),validators.MaxLengthValidator(50)])
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_bot_handler(self):
        inputbot=self.cleaned_data['bot_handler']
        if(len(inputbot))>0:
            raise forms.ValidationError("handle by bot")
        return inputbot

    def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<=6:
            raise forms.ValidationError('Name should be greater than 6 char.')
        return inputname

    def clean_password(self):
        inputpassword=self.cleaned_data['password']
        if len(inputpassword)<=8:
            raise forms.ValidationError('password should be greater than 8 char.')
        return inputpassword


    def clean(self):
        clean_data=super().clean()
        input_name=clean_data['name']
        print(input_name)                        #isse clean data ke pass sab kuch aagya bus usko use kar


'''    def clean_rpassword(self):
        inputpassword=self.cleaned_data['password']
        inputrpassword=self.cleaned_data['rpassword']
        if inputpassword!=inputrpassword:
            raise forms.ValidationError('password not match')
        return inputrpassword'''
