import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)  # replace with your key

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Path to image
image_path = "kolam3.jpeg"

# Read image as bytes
with open(image_path, "rb") as f:
    image_bytes = f.read()

# Wrap into correct format for Gemini
image_input = {
    "mime_type": "image/jpeg",   # or "image/png" if PNG
    "data": image_bytes
}

# Send image + text prompt
response = model.generate_content(
    [
        image_input,
        """You are an expert in Kolam/Rangoli cultural patterns.
        Analyze this image and respond in JSON format with:
        - grid_size (e.g., 5x5, 7x7, or unknown)
        - symmetry (rotational, reflectional, radial, or none)
        - motifs (lotus, peacock, star, abstract, etc.)
        - festival (Pongal, Sankranti, Diwali, daily, or unknown)
        - region (Tamil Nadu, Andhra, Karnataka, Maharashtra, or unknown)
        - complexity (simple, medium, complex)
        - cultural_note (1-2 line cultural meaning)."""
    ],
    generation_config={"response_mime_type": "application/json"},
)

# Print structured JSON output
print(response.text)
