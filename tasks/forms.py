from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vazifa nomi ...'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
