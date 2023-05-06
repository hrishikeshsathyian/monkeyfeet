from django import forms 
from .models import Assignment

class AssignmentForm(forms.ModelForm):
    hourly_rate = forms.DecimalField(max_digits=2,decimal_places=0)
    class Meta:
        model = Assignment
        fields = ['subject','hourly_rate','additional_information']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control' # for styling purposes make all fields contain form-control 
            field.widget.attrs['style'] = 'background-color: white !important ;'