from .models import Routine , User
from django import forms

#Modelform for user using username
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


#modelform for routine
class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = '__all__'

#Modelform for user 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

