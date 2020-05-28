from django import forms
from django.core.exceptions import ValidationError
from .models import Distance




class DistanceForm(forms.ModelForm):
    class Meta:
        model = Distance
        fields = ('cities', 'km')
    
    def clean(self):
        if len(self.cleaned_data.get('cities')) != 2:
            raise ValidationError('Расстояние только между двумя городами')