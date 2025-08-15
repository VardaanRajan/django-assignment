from django import forms
from .models import ChaiVarity

class ChaiForm(forms.ModelForm):
    class Meta:
        model = ChaiVarity
        fields = ['name', 'type', 'image', 'data_added']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter chai name'
            }),
            'type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'data_added': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            })
        }
        labels = {
            'name': 'Chai Name',
            'type': 'Chai Type',
            'image': 'Chai Image',
            'data_added': 'Date Added'
        }
        help_texts = {
            'name': 'Enter the name of your chai variant',
            'type': 'Select the type of chai',
            'image': 'Upload an image of the chai',
            'data_added': 'Date and time when chai was added'
        }