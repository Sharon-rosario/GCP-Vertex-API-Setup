import vertexai
from vertexai.generative_models import GenerativeModel, HarmCategory, HarmBlockThreshold
from google.oauth2 import service_account
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get environment variables
SERVICE_ACCOUNT_KEY_PATH = os.getenv("SERVICE_ACCOUNT_KEY_PATH")
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")

# Authenticate using service account key
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_KEY_PATH,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Initialize Vertex AI
vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)

# Initialize the model
model = GenerativeModel("gemini-1.5-pro")

# Simple prompt
prompt = "Hello! Can you tell me a fun fact about the United States?"

# Configure safety settings
safety_settings = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
}

# Generate response
response = model.generate_content(
    contents=[prompt],
    generation_config={
        "temperature": 1.0,
        "top_p": 1.0,
        "max_output_tokens": 65535,
    },
    safety_settings=safety_settings
)

# Print the response
print(response.text)