from .models import Task
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class UserTaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due', 'status']
        widgets = {'user': forms.HiddenInput(), 'date': forms.HiddenInput(), 'due': DateInput()}
