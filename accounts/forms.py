from django import forms
from .models import User 
from student.models import Student, Subject, TutorLevel
from tutors.models import Tutor
from crispy_forms.helper import FormHelper

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))
    confirm_password = forms.CharField(widget=forms.PasswordInput(render_value=True))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone_number','password']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control' # for styling purposes make all fields contain form-control 
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password :
            raise forms.ValidationError(
                "Password does not match"
            )
class StudentForm(forms.ModelForm):
    preferred_tutor_level = forms.ModelMultipleChoiceField(
        queryset= TutorLevel.objects.all(),
        widget=forms.CheckboxSelectMultiple
    ) # set to multiple select choice field
    subjects = forms.ModelMultipleChoiceField(
        queryset= Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple
    ) # set to multiple select choice field
    class Meta:
        model = Student 
        fields = ['gender','dob','profile_picture','address','zip_code','latitude','longitude','subjects','preferred_gender','additional_information','preferred_tutor_level'] 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False # removes automated labels so we can manually add them in the front end
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control' # for styling purposes make all fields contain form-control 
        self.fields['dob'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            ) # set calendar input for date of birth
        

class TutorForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        queryset= Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple
    ) # set to multiple select choice field
    qualification_information = forms.CharField(
                    widget=forms.Textarea(attrs={'rows':4,'cols':15,'placeholder': 'Please include any information that you think will help boost your credibility as a tutor. e.g Current University Course, Past Experience'}))
    
    class Meta:
        model = Tutor 
        fields = ['gender','dob','profile_picture','address','zip_code','latitude','longitude','subjects','qualification_information','certificate_credential','additional_information','tutor_level'] 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False # removes automated labels so we can manually add them in the front end
        self.fields['qualification_information'].placeholder = 'Please type here'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control' # for styling purposes make all fields contain form-control 
        self.fields['dob'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            ) # set calendar input for date of birth