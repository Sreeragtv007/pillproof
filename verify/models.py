
from django.db import models

class PrescriptionVerification(models.Model):
    prescription_image = models.ImageField(upload_to='prescriptions/')
    medicine_image = models.ImageField(upload_to='medicines/')
    verification_result = models.CharField(max_length=200, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Verification for {self.prescription_image.name}"