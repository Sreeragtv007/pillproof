import google.generativeai as genai
import PIL.Image
import os
from dotenv import load_dotenv


# --- Configuration ---
# Replace with your actual API key
load_dotenv()
# GOOGLE_API_KEY = 'AIzaSyChINg613sQ9p9vNUshJmtATTYqolT52i8'

GOOGLE_API_KEY = os.getenv("api_key")
genai.configure(api_key="AIzaSyChINg613sQ9p9vNUshJmtATTYqolT52i8")


def verify_medicine_with_prescription(prescription_image_path, medicine_image_path):

    try:
        # --- Load Images ---
        prescription_img = PIL.Image.open(prescription_image_path)
        medicine_img = PIL.Image.open(medicine_image_path)

        # --- Set Up the Model ---
        # Using the gemini-pro-vision model which can handle image inputs
        model = genai.GenerativeModel('gemini-2.5-flash')
        # --- Create the Prompt ---
        # The prompt is a list containing text instructions and the images.
        prompt_parts = [

            """
    You are an intelligent document verification assistant with expertise in processing medical documents using Optical Character Recognition (OCR).

    Your goal is to analyze the two images provided: a doctor's prescription and a pharmacy bill. You must verify that the medicines and quantities on the pharmacy bill correctly match what was prescribed.

    Perform these steps only to make the below dictionary 
    1.  Extract all text from both the prescription and the bill images or medicine image.
    2.  From the prescription, list all prescribed medicine names and their quantities.
    3.  From the bill or medicine image, list all purchased medicine names and their quantities.
    4.  Compare the two lists to find any discrepancies, such as:
        - Medicines prescribed but not billed.
        - Medicines billed but not prescribed.
        - Mismatches in quantity.

    The result must have the following exact structure,
    only give result as below format only,
    
    verified : medicine name1,medicine name2, ....
    not verified : medicine name1,medicine name2, ...
    }
    """,


            "Prescription Image: ",
            prescription_img,
            "\nMedicine Image: ",
            medicine_img,
        ]

        # --- Make the API Call ---
        response = model.generate_content(prompt_parts)

        return response.text

    except FileNotFoundError:
        return "Error: One or both image files were not found. Please check the file paths."
    except Exception as e:
        return f"An error occurred: {e}"

    """
    
     "You are a pharmacy assistant. Your task is to verify if the medicine in the second image matches the medicine name written in the first image, which is a prescription.",
            "Carefully read the prescription in the first image and identify the medicine's name.",
            "Then, look at the medicine packaging in the second image and read its name.",
            "Compare the two names.",
            "Finally, respond with either 'true' if verified or 'false' and provide a one-sentence valid explanation for your conclusion.",



    
    
    """
