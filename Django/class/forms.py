from django import forms
from .models import MRIScan

class MRIUploadForm(forms.ModelForm):
    class Meta:
        model = MRIScan
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }