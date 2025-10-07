import google.generativeai as genai
import PIL.Image
import os
from dotenv import load_dotenv


# --- Configuration ---
# Replace with your actual API key
load_dotenv()


GOOGLE_API_KEY = os.getenv("api_key")
genai.configure(api_key="AIzaSyChINg613sQ9p9vNUshJmtATTYqolT52i8")   # REPLACE GEMINI API KEY HERE


def verify_medicine_with_prescription(prescription_image, text):

    try:

        # --- Set Up the Model ---
        # Using the gemini-pro-vision model which can handle image inputs
        model = genai.GenerativeModel('gemini-2.5-pro')
        # --- Create the Prompt ---
        # The prompt is a list containing text instructions and the images.
        prompt_parts = [


            '''
            **Context:** You are a highly accurate prescription verification AI. You will receive one image and text of the medicine for analysis.

**Objective:** Analyze the prescription and the medicine text, perform a step-by-step comparison, and provide a final verification status in a structured format.

**Step-by-Step Instructions:**
1.  **Analyze Prescription Image:** Carefully read the text on the prescription. Identify and extract the prescribed medicine's name and dosage.
2.  **Analyze Medicine ocr text :** Carefully read the text given. Identify and extract the brand name, the generic name, and the dosage.
3.  **Compare:** Compare the extracted information from image and text. Check if the medicine name of the medicine matches what was prescribed. Also, confirm the dosage matches.
4.  **Conclude:** Based on the comparison, decide if the medicine is verified or not.

**Final Output Specification:**
After completing your analysis, provide your response in the following format. Do not include any other text or explanation.

**If the verification is successful:**
Verified
Medicine: [Name of the medicine from the package]

**If the verification fails:**


[Provide a brief reason, e.g., " medicine mismatch"]''',



            "Prescription Image: ",
            prescription_image,
            "\nMedicine text: ", text
            # medicine_image,
        ]

        # --- Make the API Call ---
        response = model.generate_content(prompt_parts)

        return response.text

    except Exception:
        return False

  
