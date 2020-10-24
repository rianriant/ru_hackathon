from django.forms import ModelForm
from .models import Ivent
from django.forms import DateTimeInput
from tinymce.widgets import TinyMCE
from ruhackathon import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Row, Column


class IventDateTimeForm(DateTimeInput):
    """A widget for much convinient usage of Date field"""
    input_type = 'date'

class IventCreateForm(ModelForm):
    """A form for creating an ivent, tied with IventCreateView"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'iventCreateForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

        # Name of the route where the post request is addressed to:
        self.helper.form_action = 'ivent-create'

        self.helper.layout = Layout(

                Row(
                    Column('title', css_class="col-sm-12"),
                ),
                Row(
                    Column('description', css_class="col-sm-12"),
                ),
                Row(
                    Column('reg_start_date', css_class="col-sm-3"),
                    Column('reg_finish_date', css_class="col-sm-3"),
                    Column('ivent_start_date', css_class="col-sm-3"),
                    Column('ivent_finish_date', css_class="col-sm-3"),
                ),
                ButtonHolder(
                    Submit('submit', 'Submit', css_class='btn-primary')
                ),
        )

    
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

   