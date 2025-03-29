from google import genai
from PIL import Image
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()

# Set and validate API key
API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY is None:
    raise ValueError("Please add your API key to the .env file as GEMINI_API_KEY=your_key_here")


def audio_to_text(audio_file_path):
    client = genai.Client(api_key=API_KEY)

    myfile = client.files.upload(file=audio_file_path)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=['Describe this audio clip', myfile]
        )
    # Files are automatically deleted after 48 hours. Optionally, you can manually delete an uploaded file.
    client.files.delete(name=myfile.name)
    return response.text

