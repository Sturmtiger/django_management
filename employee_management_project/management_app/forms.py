from django import forms
from django.utils import timezone

from .models import WorkTime


class WorkTimeForm(forms.ModelForm):
    """WorkTime form."""
    class Meta:
        model = WorkTime
        fields = ('workplace', 'date', 'hours_worked')

    def clean_date(self):
        data = self.cleaned_data['date']
        if data != timezone.localdate():
            raise forms.ValidationError('Date must be today')
        return data