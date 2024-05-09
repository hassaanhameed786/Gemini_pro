from fastapi import FastAPI, File, UploadFile
import textwrap
from PIL import Image
import os
from vertexai.preview.generative_models import GenerativeModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GENERATIVE_MODEL_NAME = "gemini-1.0-pro-vision"
def configure_genai(api_key)
    """
    :param api_key: from google vertex api (Gcloud)
    :return: none
    """
    import google.generativeai as genai
    genai.configure(api_key=api_key)

def generate_content(image_filename):
    """
    :param image_filename:
    :return:  image analysis and img is about description and category and estimate price
    """
    gemini_pro_vision_model = GenerativeModel(GENERATIVE_MODEL_NAME)
    model_response = gemini_pro_vision_model.generate_content(["what is this image title? and description and category and estimate price", image_filename])
    print(model_response)
    return model_response.text

@app.post("/generate")
async def generate_image_content(image: UploadFile = File(...)):
    """
    :param image:
    :return:
    """
    with open(image.filename, "wb") as buffer:
        buffer.write(image.file.read())

    configure_genai(GOOGLE_API_KEY)
    model_text = generate_content(image.filename)
    print(model_text)
    return {"response": model_text}

