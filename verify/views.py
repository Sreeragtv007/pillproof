# verifier_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
import PIL
from .models import PrescriptionVerification
from .gemini_verify import verify_medicine_with_prescription
import json


def upload_view(request):
    if request.method == 'POST':

        priscription = request.FILES['priscription']
        medicine = request.FILES['medicine']

        prescription_img = PIL.Image.open(priscription)
        medicine_img = PIL.Image.open(medicine)

        result = verify_medicine_with_prescription(
            prescription_img, medicine_img)

        print(type(result))
        print(result)

        context = {'result': result}

        return render(request,'result.html',context)
    else:

        return render(request, 'upload1.html')


def result_view(request):

    return render(request, 'result.html')
