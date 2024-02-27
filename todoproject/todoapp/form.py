from.models import Ttask
from django import forms

class todoform(forms.ModelForm):
    class Meta:
        model=Ttask
        fields=['name','priority','date']
