from django.shortcuts import render
from testapp import forms
# Create your views here.

def thankyou_view(request):
    return render(request,'templatetestapp/thankyou.html')

def feedbackview(request):
    form=forms.feedbackform()  #sabse phele get method chalta he to feedback form provide karega
    if request.method=='POST':
        form=forms.feedbackform(request.POST)# bhai data bhi to chaiye
        if form.is_valid():
            print('form validation success and print info')
            print("Student name :",form.cleaned_data['name'])
            print("Student age :",form.cleaned_data['age'])
            print("Student password :",form.cleaned_data['password'])
            print("Student rpassword :",form.cleaned_data['rpassword'])
            print("Student email :",form.cleaned_data['email'])
            print("Student feedback :",form.cleaned_data['feedback'])
            return thankyou_view(request)
    return render(request,'templatetestapp/feedback.html',{'form':form})
