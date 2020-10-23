from django.forms import ModelForm
from .models import Ivent
from django.forms import DateTimeInput
from tinymce.widgets import TinyMCE
from ruhackathon import settings


class IventDateTimeForm(DateTimeInput):
    """A widget for much convinient usage of Date field"""
    input_type = 'date'

class IventCreateForm(ModelForm):
    """A form for creating an ivent, tied with IventCreateView"""
    
    class Meta:
        model = Ivent

        widgets = {
            #'description': TinyMCE(mce_attrs={'theme' : 'advanced'}),
            'reg_start_date': IventDateTimeForm,
            'reg_finish_date': IventDateTimeForm,
            'ivent_start_date': IventDateTimeForm,
            'ivent_finish_date' : IventDateTimeForm,
        }
        
        
        fields = ['title', 'description',
        'reg_start_date','reg_finish_date', 'ivent_start_date', 'ivent_finish_date',
        'area', 'address']

   