# verifier_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
import PIL
from .models import PrescriptionVerification
from .gemini_verify import verify_medicine_with_prescription
import json
from datetime import datetime
import pytesseract

def upload_view(request):
    if request.method == 'POST':
        start = datetime.now()

        priscription = request.FILES['priscription']
        medicine = request.FILES['medicine']
        
       

        prescription_img = PIL.Image.open(priscription)
        medicine_img = PIL.Image.open(medicine)
        
        text = pytesseract.image_to_string(medicine_img)
        print(text)

        result = verify_medicine_with_prescription(
            prescription_img, medicine_img)

        print(type(result))
        print(result)

        context = {'result': result}
        end = datetime.now()
        print(end-start)

        return render(request,'result.html',context)
    else:

        return render(request, 'upload1.html')


def result_view(request):

    return render(request, 'result.html')
