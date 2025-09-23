# verifier_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from .models import PrescriptionVerification
from django.conf import settings
import os
import crewai
from .agent import verify_prescription_crew



def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database, including the image files
            verification_entry = form.save(commit=False)
            
            # CrewAI Integration
            # The files are now saved, you can access their paths
            prescription_path = verification_entry.prescription_image.path
            medicine_path = verification_entry.medicine_image.path
            
            # Run the CrewAI verification
            result = verify_prescription_crew(prescription_path, medicine_path)
            
            # Save the result to the model instance before committing
            verification_entry.verification_result = result
            verification_entry.save()
            
            return redirect('result_view', result=result)
    else:
        form = UploadForm()
    
    return render(request,'upload.html', {'form': form})

def result_view(request, result):
    # This view will display the verification result.
    return render(request,'result.html', {'result': result})

