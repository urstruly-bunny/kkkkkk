from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Set up environment variables for LangChain tracing (if needed)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Define Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to user queries."),
    ("user", "Question={question}")
])

# Streamlit UI
st.title('LangChain with Llama 3.2')
input_text = st.text_input("Enter your question:")

# Debugging
st.write("Debug Input:", input_text)

# Initialize Ollama LLM
llm = Ollama(model="phi", base_url="http://127.0.0.1:11434")

# Create LangChain pipeline
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({'question': input_text})
    st.write("Response:", response)
