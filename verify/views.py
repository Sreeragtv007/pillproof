# verifier_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from .models import PrescriptionVerification
from django.conf import settings
import os
# import crewai
from .agent import verify_prescription_crew
from .gemini_verify import verify_prescription_gemini


def upload_view(request):
    if request.method == 'POST':

        prescription_file = request.FILES.get("priscription")
        medicine_file = request.FILES.get("medicine")

        obj = PrescriptionVerification.objects.create(
            prescription_image=prescription_file, medicine_image=medicine_file)

        # Run the CrewAI verification
        result = verify_prescription_gemini(
            obj.prescription_image.path, obj.medicine_image.path)

        # Save the result to the model instance before committing
        obj.verification_result = result
        obj.save()
        context = {"result": result}
        return render(request, 'result.html', context)
    else:

        return render(request, 'upload.html')


def result_view(request):
    # This view will display the verification result.
    return render(request, 'result.html')
