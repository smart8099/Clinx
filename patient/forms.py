from django.forms import ModelForm
from .models import PatientInfo,OPD
from django import forms


class PatientInfo_Form(forms.ModelForm):
    class Meta:
        model = PatientInfo
        fields="__all__"
        widgets = {
            'gender': forms.RadioSelect()
        }
class OPD_DataForm(forms.ModelForm):
    class Meta:
        model = OPD
        fields="__all__"
