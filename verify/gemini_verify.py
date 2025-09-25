import google.generativeai as genai
from PIL import Image
import base64
import google.genai as genai
from google.genai import types

# Configure Gemini
# genai.configure(api_key="AIzaSyChINg613sQ9p9vNUshJmtATTYqolT52i8")

client = genai.Client(api_key="AIzaSyChINg613sQ9p9vNUshJmtATTYqolT52i8")




def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")



def verify_prescription_gemini(prescription_path, medicine_path):
    prescription_b64 = image_to_base64(prescription_path)
    medicine_b64 = image_to_base64(medicine_path)

    # Construct the multimodal prompt
    prompt = [
        types.Message(
            role="user",
            content=[
                {"type": "text", "text": "Verify if the prescription and the medicine image match. Answer only 'Verified' or 'Not Verified' with a short reason."},
                {"type": "image", "image": prescription_b64},
                {"type": "image", "image": medicine_b64}
            ]
        )
    ]

    # Send the prompt to the model
    # response = client.chat(messages=prompt, model="gemini-1.5-flash")
    
    response = client.chats.create(messages=prompt, model="gemini-1.5-flash")

    return response.content[0].text.strip()
