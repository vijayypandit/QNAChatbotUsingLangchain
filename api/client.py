import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] =os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

def get_grok_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
                            json={'input':{'topic':input_text}})
    return response.json()['output']['content']

st.title("Langchain Demo With Groq API chains")
input_text=st.text_input("Write An Essay On")

if input_text:
    st.write(get_grok_response(input_text))

