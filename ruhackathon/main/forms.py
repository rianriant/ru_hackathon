from django.forms import ModelForm
from .models import Ivent
from django.forms import DateTimeInput
#from tinymce.widgets import TinyMCE

class IventDateTimeForm(DateTimeInput):
    """A widget for much convinient usage of Date field"""
    input_type = 'date'

class IventCreateForm(ModelForm):
    """A form for creating an ivent, tied with IventCreateView"""
    class Meta:
        widgets = {
            #'description' : TinyMCE(attrs={'cols': 80, 'rows': 3}),
            'reg_finish_date' : IventDateTimeForm,
            
        }
        model = Ivent
        fields = ['title', 'description',
        'reg_start_date','reg_finish_date', 'ivent_start_date', 'ivent_finish_date',
        'area', 'address']

   