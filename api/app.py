from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


app=FastAPI(
    title="My Langchain server",
    version="1.0",
    description="A simple api server"

)

llm1=Ollama(model="gemma:2b")
llm2=Ollama(model="phi")

prompt1=ChatPromptTemplate.from_template("Write an essay about {topic} in 100 words")
prompt2=ChatPromptTemplate.from_template("Write an poem about {topic} in 100 words")


add_routes(
    app,
    prompt1 | llm1,
    path="/essay"
)

add_routes(
    app,
    prompt2 | llm2,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)