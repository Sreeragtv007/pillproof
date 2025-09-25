import google.generativeai as genai
import PIL.Image

# --- Configuration ---
# Replace with your actual API key
GOOGLE_API_KEY = 'AIzaSyChINg613sQ9p9vNUshJmtATTYqolT52i8'
genai.configure(api_key=GOOGLE_API_KEY)

def verify_medicine_with_prescription(prescription_image_path, medicine_image_path):
   
    try:
        # --- Load Images ---
        prescription_img = PIL.Image.open(prescription_image_path)
        medicine_img = PIL.Image.open(medicine_image_path)

        # --- Set Up the Model ---
        # Using the gemini-pro-vision model which can handle image inputs
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        # --- Create the Prompt ---
        # The prompt is a list containing text instructions and the images.
        prompt_parts = [
            "You are a pharmacy assistant. Your task is to verify if the medicine in the second image matches the medicine name written in the first image, which is a prescription.",
            "Carefully read the prescription in the first image and identify the medicine.",
            "Then, look at the medicine packaging in the second image and read its name.",
            "Compare the two names.",
            "respond with either 'Verified' or 'Not Verified' and provide a one-sentence which medicine are verified and explanation for your conclusion.",
            
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

