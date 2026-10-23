from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI
from langserve import add_routes

import uvicorn
import os
from dotenv import load_dotenv

load_dotenv(override=True)

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

# Create a FastAPI application instance
app=FastAPI(
    title="LangServe Server", 
    description="A Simple API Server", 
    version="1.0"
    )

# LangServe is used to deploy LangChain applications as APIs 
# so that other applications can access them over HTTP.
add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

openai_model=ChatOpenAI()
ollama_model=OllamaLLM(model="llama2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

add_routes(    
    app,
    prompt1|openai_model,
    path="/essay"
)

add_routes(    
    app,
    prompt2|ollama_model,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)