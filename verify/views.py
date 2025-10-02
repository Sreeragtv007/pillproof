# verifier_app/views.py
from django.shortcuts import render
import PIL
from .gemini_verify import verify_medicine_with_prescription
from datetime import datetime
import pytesseract


def upload_view(request):
    if request.method == 'POST':
        start = datetime.now()

        priscription = request.FILES['priscription']
        medicine = request.FILES['medicine']

        prescription_img = PIL.Image.open(priscription)
        medicine_img = PIL.Image.open(medicine)
        
        try:

            text = pytesseract.image_to_string(medicine_img)
        except:
            context ={"result":"unexpected error from ocr"}
            return render(request,'result.html',context)

        result = verify_medicine_with_prescription(
            prescription_img, text)

        print(type(result))
        print(result)
        
        if result == False:
            context ={"result":"unexpected error form api"}
            return render(request,'result.html',context)
            

        context = {'result': result}
        end = datetime.now()
        print(end-start)

        return render(request, 'result.html', context)
    else:

        return render(request, 'upload1.html')

