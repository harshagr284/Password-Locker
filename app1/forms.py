from app1.models import Password1
from django import forms
from app1.models import Password1
class Passform(forms.ModelForm):
    class Meta:
        model=Password1
        fields={'title','password'}
