import google.generativeai as genai
from PIL import Image

# Configure Gemini
genai.configure(api_key="AIzaSyChINg613sQ9p9vNUshJmtATTYqolT52i8")
model = genai.GenerativeModel("gemini-1.5-flash")

def verify_prescription_gemini(prescription_path, medicine_path):
    # Load images directly from file paths
    prescription_img = Image.open(prescription_path)
    medicine_img = Image.open(medicine_path)

    # Ask Gemini to compare
    response = model.generate_content([
        "Verify if the prescription and the medicine image match. "
        "Answer only 'Verified' or 'Not Verified' with a short reason.",
        prescription_img,
        medicine_img
    ])

    return response.text.strip()
