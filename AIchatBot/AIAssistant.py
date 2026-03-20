from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain_groq import ChatGroq


import streamlit as st
import os 
from dotenv import load_dotenv
load_dotenv()

##Created using Opensource GROQ api --------------
#env variable calls 

groq_api_key = os.getenv("GROQ_API_KEY")
if groq_api_key:
    os.environ["GROQ_API_KEY"] = groq_api_key

os.environ["LANGCHAIN_API_KEY"] =os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

#Creating chatbot###

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to user queries."),
        ("user","Question:{question}")
    ]
)

#Streamlit framework -for ui related

st.title("Your AI Assistant ! Langchain Demo Test With Groq API")
input_text=st.text_input("Search the topic you want to Query ? !")

#LLM Call

model=ChatGroq(model="llama-3.1-8b-instant")
output_parser=StrOutputParser()

#Chain creation
chain=prompt|model|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
