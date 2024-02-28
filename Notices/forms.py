from django import forms
from .models import Drive,Activity,Department



class DriveForm(forms.ModelForm):
    class Meta:
        model = Drive
        fields = ['title', 'company_name', 'company_logo', 'date', 'content', 'Bond', 'industry_type', 'department', 'job_role', 'job_location', 'job_eligibility', 'selection_process', 'job_CTC']

        widgets = {
            'department': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(DriveForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs['class'] = 'form-control'
            if name == 'date':
                field.widget.attrs['placeholder'] = 'YYYY-MM-DD'


        
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'  # You can specify specific fields if needed

        widgets = {
            'department': forms.CheckboxSelectMultiple()
        }
    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs['class'] = 'form-control'
            if name == 'activity_date':
                field.widget.attrs['placeholder'] = 'YYYY-MM-DD'