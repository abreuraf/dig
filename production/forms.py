from django import forms
from .models import Production

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ('__all__')