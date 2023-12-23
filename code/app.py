from dotenv import load_dotenv
load_dotenv() # load the enviornments vars

# import libs
import streamlit as st
import os
import google.generativeai as genai

# configure the apikey
genai.configure(api_key=os.getenv("google_api"))

model = genai.GenerativeModel('gemini-pro')   # Generate text from text input

# function to load the model and get responses from the model
def get_gemini(ask_what_ulike):
    response =model.generate_content(ask_what_ulike)
    return  response.text


# Add a title to your app
st.set_page_config(page_title="hello_gemni")

st.header('Gemini LLM App')
st.subheader('Your personal language model assistant')

input=st. text_input ("Input: ",key="input")
submit=st. button("Ask the question")
## When submit is clicked
if submit:
    response=get_gemini(input)
    st. subheader ("The Response is")
    st. write (response)