from django import forms

from . models import my_class

BIRTH_YEAR_CHOICES = ['2001', '2002', '2003' , '2004' , '2005']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
FAVORITE_COLORS_CHOICES1 = [
    ('Mango', 'Lichie'),
    ('Date', 'Apple'),
    ('Jackfruit', 'Pudding'),
]
class my_forms(forms.Form):
    name = forms.CharField(max_length=20)
    email= forms.EmailField(max_length=100,
                           widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))
    agree = forms.BooleanField( initial= 'True or False' )
    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))    
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    message = forms.CharField(max_length = 10 ,initial= 'Only 10 Word are allow')
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    favorite_colors = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES1)

    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    
    

