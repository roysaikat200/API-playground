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


def Text_and_image_input(img):
    client = genai.Client(api_key=API_KEY)

    image = Image.open(img)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction = '''You are a simple AI assistant.''',  
            temperature = 0.7,
            topP = 0.85,
            topK = 40,
            maxOutputTokens = 500,
            candidateCount = 1,
            presencePenalty = 0.2,
            frequencyPenalty = 0.4,
            responseModalities = ["TEXT"]
            ),
        contents=[image, "ignore any logo if exists", "Describe the image."]
        )
    # print(response.text)
    # print(type(response))
    return response.text

def Img_Classification(img1, img2):
    client = genai.Client(api_key=API_KEY)

    image1 = Image.open(img1)
    image2 = Image.open(img2)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction = '''You are a simple AI assistant.''',  
            temperature = 0.7,
            topP = 0.85,
            topK = 40,
            maxOutputTokens = 500,
            candidateCount = 1,
            presencePenalty = 0.2,
            frequencyPenalty = 0.4,
            responseModalities = ["TEXT"]
            ),
        contents=[image1, image2, "Classify these images and find wht is different among them."]
        )
    # print(response.text)
    # print(type(response))
    return response.text

img = 'img/Veronica.png' # png file is supported
response = Text_and_image_input(img=img)
print(response)

# img = 'img/Mango.jpg' # jpg file is supported
# response = Text_and_image_input(img=img)

# img1 = "img/Apple.jpg"
# img2 = "img/Mango.jpg"
# response = Img_Classification(img1=img1, img2=img2)
# print(response)
