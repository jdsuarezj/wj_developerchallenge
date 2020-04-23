from django import forms
from django.contrib.auth.models import User

# Form for the url input
class ScanForm(forms.Form):
    urlInput = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Paste here the URL",
                "class": "form-control"
            }
        ))    

    class Meta:
        model = User
        fields = ('urlInput')
