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
        
        
        priscription = request.FILE.get('priscription')
        medicine = request.FILE.get('medicine')
        
        obj = PrescriptionVerification.objects.create(prescription_image=priscription,medicine_image=medicine)
        
        
        
        
            
            
            
        return redirect('result_view',)
    else:
        form = UploadForm()
    
    return render(request,'upload.html', {'form': form})

def result_view(request, result):
    # This view will display the verification result.
    return render(request,'result.html', {'result': result})

