from django import forms
from .models import Tools

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tools
        fields = ['icon_class', 'name', 'description']
        widgets = {
            'icon_class': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. bi-hammer'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tool name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Short description'
            }),
        }