from django import forms
from .models import New


class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = '__all__'

        widgets = {
            'type': forms.TextInput(attrs={
                'placeholder': 'Yangilik turi',
                'class': 'form-control',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'turi': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'type': 'jahon yoki ichki',
            'text': 'Text',
            'turi': 'yangilik turi',
            'name': 'muallif ismi'
        }