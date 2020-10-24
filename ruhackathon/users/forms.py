from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Row, Column


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'registerForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

        # Name of the route where the post request is addressed to:
        self.helper.form_action = 'register'

        self.helper.layout = Layout(
                Row(
                Column('username', css_class="col-md-6 col-sm-12"),
                Column('email', css_class="col-md-6 col-sm-12"),
                ),
                Row(
                Column('password1', css_class="col-md-6 col-sm-12"),
                Column('password2', css_class="col-md-6 col-sm-12"),
                ),
                ButtonHolder(
                    Submit('submit', 'Submit', css_class='btn-dark btn')),
        )

        # Description for the submit-typed button with sign "Submit":
        # self.helper.add_input(Submit('submit', 'Submit'))

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpadateForm(forms.ModelForm):

     class Meta:
        model = Profile
        fields = ['image']