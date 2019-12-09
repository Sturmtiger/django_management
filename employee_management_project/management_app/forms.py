from django import forms
from .models import WorkTime


class WorkTimeForm(forms.ModelForm):
    """WorkTime form."""
    class Meta:
        model = WorkTime
        fields = ['workplace', 'date_start', 'date_end']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("date_start")
        end_date = cleaned_data.get("date_end")

        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")
