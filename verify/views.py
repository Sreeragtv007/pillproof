# verifier_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from .models import PrescriptionVerification
from django.conf import settings
import os
import crewai



def upload_view(request):
    if request.method == 'POST':
        
        
        priscription = request.FILES['priscription']
        medicine = request.FILES['medicine']
        
        obj = PrescriptionVerification.objects.create(prescription_image=priscription,medicine_image=medicine)
        
             
        
            
            
            
        return render(request,'result.html')
    else:
        
    
        return render(request,'upload.html')

def result_view(request, result):
    # This view will display the verification result.
    return render(request,'result.html', {'result': result})

