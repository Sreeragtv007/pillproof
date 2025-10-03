# 1. Base Image
# Use an official Python runtime as a parent image. 'slim' is a good choice for smaller image sizes.
FROM python:3.11-slim

# 2. Set Environment Variables
# Prevents Python from writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures Python output is sent straight to the terminal without buffering
ENV PYTHONUNBUFFERED 1

# 3. Install System Dependencies for Tesseract
# We need to install the tesseract-ocr engine itself, not just the Python wrapper.
# 'tesseract-ocr-eng' is the English language pack. Add others if you need them (e.g., tesseract-ocr-fra).
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    && apt-get clean

# 4. Set the Working Directory
WORKDIR /app

# 5. Install Python Dependencies
# We copy requirements.txt first to leverage Docker's layer caching.
# If requirements.txt doesn't change, this layer won't be rebuilt, speeding up subsequent builds.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy Project Code
# Copy the rest of your application's code into the container.
COPY . .

# 7. Expose Port
# Tell Docker the container listens on port 8000
EXPOSE 8000

# 8. Command to Run the Application
# The '0.0.0.0' is crucial to make the server accessible from outside the container.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]