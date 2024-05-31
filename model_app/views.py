from django.shortcuts import render,redirect
from . import forms

# Create your views here.

def models(request):
    if request.method == 'POST' :
        my_forms = forms.my_form(request.POST)
        if my_forms.is_valid():
            my_forms.save()
            return redirect('models')   
    else: 
        my_forms = forms.my_form()
    return render(request, 'model.html' , {'data' : my_forms})