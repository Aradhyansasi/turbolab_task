from django import forms
from .models import Datas

class CSVForm(forms.ModelForm):
    class Meta:
        model= Datas
        fields = [
            'file_name',
            'count'
        ]
    # name = forms.CharField(max_length=120, required=True)
    # count = forms.CharField(max_length=120, required=True)