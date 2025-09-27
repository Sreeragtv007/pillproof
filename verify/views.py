# verifier_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import PrescriptionVerification
from .gemini_verify import verify_medicine_with_prescription


def upload_view(request):
    if request.method == 'POST':

        priscription = request.FILES['priscription']
        medicine = request.FILES['medicine']

        obj = PrescriptionVerification.objects.create(
            prescription_image=priscription, medicine_image=medicine)

        medicine_path = obj.medicine_image.path
        priscription_path = obj.prescription_image.path
        
        result = verify_medicine_with_prescription(medicine_path,priscription_path)
        
        context = {"result":result}
        
        print('test')
        print(result)
        
        return HttpResponse(result)
        
        return render(request, 'result.html',context)
    else:

        return render(request, 'upload1.html')


def result_view(request):
    
    return render(request, 'result.html')
