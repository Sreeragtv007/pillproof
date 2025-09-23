from crewai import Agent, Task, Crew, Process
from crewai_tools import ImageAnalysisTool
from langchain_google_genai import ChatGoogleGenerativeAI

# --- Add your Gemini API key here ---
GEMINI_API_KEY = ""

# Configure Gemini LLM (vision-enabled)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",   # or "gemini-1.5-pro" for more accuracy
    temperature=0.2,
    google_api_key=GEMINI_API_KEY
)

def verify_prescription_crew(prescription_path: str, medicine_path: str) -> str:
    """
    Verify if a medicine bill/image matches a doctor's prescription using Gemini LLM with CrewAI.
    """

    vision_tool = ImageAnalysisTool()

    # Agent 1: Extract details from prescription
    prescription_analyst = Agent(
        role='Prescription Analyst',
        goal='Extract medicine name, dosage, and frequency from a prescription image.',
        backstory="You are skilled at interpreting prescriptions, even messy handwriting.",
        tools=[vision_tool],
        llm=llm,
        verbose=True
    )

    # Agent 2: Verify medicine bill against prescription
    medicine_verifier = Agent(
        role='Medicine Verifier',
        goal='Compare prescription details with the medicine bill/image.',
        backstory="You ensure the dispensed medicine matches exactly what was prescribed.",
        tools=[vision_tool],
        llm=llm,
        verbose=True
    )

    # Task 1: Analyze prescription (actually passes the image)
    analyze_prescription_task = Task(
        description="Analyze the prescription image and extract medicine details.",
        agent=prescription_analyst,
        expected_output="List medicines with dosage and frequency.",
        input_files=[prescription_path]   # 👈 Passes prescription image
    )

    # Task 2: Compare with medicine bill (actually passes the image)
    compare_and_verify_task = Task(
        description="Compare the extracted prescription details with the medicine bill/image.",
        agent=medicine_verifier,
        context=[analyze_prescription_task],   # 👈 Uses result from Task 1
        expected_output="Verdict: MATCH or MISMATCH with explanation.",
        input_files=[medicine_path]            # 👈 Passes medicine bill image
    )

    # Crew setup
    verification_crew = Crew(
        agents=[prescription_analyst, medicine_verifier],
        tasks=[analyze_prescription_task, compare_and_verify_task],
        process=Process.sequential,  # run tasks in order
        verbose=2
    )

    # Run the workflow
    result = verification_crew.kickoff()
    return result

# # --- Example usage ---
# if __name__ == "__main__":
#     result = verify_prescription_crew("prescription.jpg", "medicine_bill.jpg")
#     print("\n=== Final Result ===\n", result)
