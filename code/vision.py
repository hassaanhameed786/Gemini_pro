import warnings 
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("google_api"))

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-pro-vision')

# Function to generate content from an input text
def get_gemini_response(input, image):

    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)

    return response.text

# Set Streamlit app title
st.title("Image Upload and Generation App")

# Create a file uploader widget for images
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Create a text input for user's request
user_request = st.text_input("Ask Gemini what you'd like to see in the image")

# Check if an image has been uploaded
if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # You can perform further processing on the image here if needed

    # Add a button to generate content with Gemini
    if st.button("Generate Content"):
        if user_request:
            # Generate content using Gemini and user's request
            gemini_response = get_gemini_response(user_request, image)
            st.write("Gemini Content: ", gemini_response)
        else:
            st.write("Please enter a request for Gemini.")

# Add any other content or instructions you want
st.write("Upload an image and provide a request for Gemini to generate content for the image.")
