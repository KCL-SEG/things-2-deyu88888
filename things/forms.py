from django.db import models
from django import forms
from .models import Thing


"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 30}),
            'quantity': forms.NumberInput()
        }