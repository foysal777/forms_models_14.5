from django.shortcuts import render
from . forms import my_forms

# Create your views here.
def form(request):
    forms = my_forms(request.POST)
    if forms.is_valid():
        print(forms.cleaned_data)
        
    return render(request, 'form.html' , {'data' : forms})

