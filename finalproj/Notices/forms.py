

# forms.py
from django import forms
from .models import Drive

class DriveForm(forms.ModelForm):
    class Meta:
        model = Drive
        fields = '__all__'  # You can specify specific fields if needed
