from django import forms

class UploadFileForm(forms.Form):
    bom_name = forms.CharField(max_length=255)
    bom_file = forms.FileField()
    bom_version = forms.CharField(max_length=255)
    name_enterprise = forms.CharField(max_length=255)
    contact = forms.CharField(max_length=255)
    info = forms.CharField(max_length=255)
    date_production = forms.DateTimeField()
    date_return = forms.DateTimeField()
