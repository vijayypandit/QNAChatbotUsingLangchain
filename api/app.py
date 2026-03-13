from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()

import uvicorn
import os
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server for Langchain"
)

add_routes(
    app,
    ChatGroq(model="llama-3.1-8b-instant"),
    path="/groq"
)

model=ChatGroq(model="llama-3.1-8b-instant")

prompt=ChatPromptTemplate.from_template("write an essay about {topic} with 1000 words ")

add_routes(
    app,
    prompt|model,
    path="/essay"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)