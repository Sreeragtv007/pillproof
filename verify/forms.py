# verifier_app/forms.py
from django import forms
from .models import PrescriptionVerification

class UploadForm(forms.ModelForm):
    class Meta:
        model = PrescriptionVerification
        fields = ['prescription_image', 'medicine_image']