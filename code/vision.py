rom dotenv import load_dotenv
load_dotenv() # load all env vars
import os
import streamlit as st
import google.generativeai as genai


# configure the apikey
genai.configure(api_key=os.getenv("google_api"))

# here i use Vision model

model = genai.GenerativeModel('gemini-pro-vision')   #

# write a funciton for the image input form model
