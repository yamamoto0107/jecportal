from django import forms
from .models import Attend
 
 
class AttendForm(forms.ModelForm):
    class Meta:
        model = Attend
        fields = (  'number',
                    'nationality',
                    'name',
                    'kana',
                    'gender',
                    'email',
                    'abbre')