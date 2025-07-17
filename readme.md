# Vertex AI Test Project
This project demonstrates how to use Google Cloud's Vertex AI with the Gemini 1.5 Pro model to generate content.
Summary

# Set up a Google Cloud project
Create and download a service account JSON key
Configure environment variables
Install dependencies
Run the Vertex AI test script

# Prerequisites

Python 3.8 or higher
Google Cloud account
Basic command-line knowledge

# Step-by-Step Setup Instructions

Create a Google Cloud Project

Go to the Google Cloud Console
Click "Select a project" > "New Project"
Enter a project name and create the project
Note the Project ID (e.g., gen-lang-client-0367976351)


# Enable Vertex AI API

In the Google Cloud Console, navigate to "APIs & Services" > "Library"
Search for "Vertex AI API"
Click "Enable"


# Create a Service Account

In the Google Cloud Console, go to "IAM & Admin" > "Service Accounts"
Click "Create Service Account"
Enter a name (e.g., vertex-ai-service-account)
Grant the "Vertex AI User" role
Click "Done"


# Generate and Download Service Account Key

In the Service Accounts list, click on your new service account
Go to the "Keys" tab
Click "Add Key" > "Create new key"
Select "JSON" as the key type
Click "Create" to download the JSON key file
Save the file securely (e.g., as gen-lang-client-03453476351-9c3455342e0.json)


# Set Up Environment Variables

Create a .env file in the project root
Add the following to .env:PROJECT_ID=your-project-id
SERVICE_ACCOUNT_KEY_PATH=path/to/your-service-account-key.json
LOCATION=us-central1


# Replace your-project-id with your actual Project ID
Replace path/to/your-service-account-key.json with the path to your downloaded JSON key file


# Set Up Virtual Environment
python -m venv vertex_env

# Activate Virtual Environment
On Windows:
vertex_env\Scripts\activate

On macOS/Linux:source 
vertex_env/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Run the Script
python vertex_ai_test.py



# Project Structure
project_root/
│── .env
│── vertex_ai_test.py
│── requirements.txt
│── vertex_env/
│── gen-lang-client-0367976351-01bd59c8f2e0.json

# Notes

Keep the service account JSON key file secure and never commit it to version control
The .env file should be added to .gitignore
Ensure the LOCATION variable matches your intended Google Cloud region
