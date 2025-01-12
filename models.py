import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

# Step 1: Load environment variables from .env file
load_dotenv(".env")

# Step 2: Retrieve Azure OpenAI environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")

# Step 3: Initialize the Azure OpenAI model with required parameters
model = AzureChatOpenAI(
    azure_deployment="gpt-4o-mini",  # Your Azure deployment
    api_version=OPENAI_API_VERSION,  # Your API version
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    temperature=0,  # Controls randomness; 0 is more deterministic
    max_tokens=None,  # Set according to your needs
    timeout=None  # Adjust if needed
)