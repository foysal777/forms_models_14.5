from django import forms
from datetime import datetime
from .models import my_model

class my_form(forms.ModelForm):
    
    date_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'Select a date and time'
            }
        )
    )

    time_field = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'value': datetime.now().strftime('%H:%M:%S'),
                'class': 'form-control',
                'placeholder': 'Select time'
            }
        )
    )
    
    today_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'value': datetime.now().strftime('%Y-%m-%d'),
                'class': 'form-control',
                'placeholder': 'Select date'
            }
        )
    )

    
    class Meta:
        model = my_model
        fields = '__all__'
        
        
        
        
        