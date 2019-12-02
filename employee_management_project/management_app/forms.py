from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    """Job form."""
    class Meta:
        model = Job
        fields = ['company', 'name']
