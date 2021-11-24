from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
# Reordering Form and View
class PositionForm(forms.Form):
    position = forms.CharField()



class RegisterationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['is_superuser', 'groups','user_permissions','is_active','active']