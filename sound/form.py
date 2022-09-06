from django import forms
from .models import UploadField

class FF(forms.ModelForm):
    class Meta:
        model = UploadField
        fields = ['file']