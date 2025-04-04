import requests
import streamlit as st

def get_gemma_response(input_text):
    response = requests.post(
        "http://0.0.0.0:8000/essay/invoke",
        json={"input": {"topic": input_text}}  # Corrected JSON format
    )

    try:
        return response.json()["output"]
    except requests.exceptions.JSONDecodeError:
        return "Error: Invalid JSON received from server"

def get_phi_response(input_text):
    response = requests.post(
        "http://0.0.0.0:8000/poem/invoke",
        json={"input": {"topic": input_text}}  # Corrected JSON format
    )

    try:
        return response.json()["output"]
    except requests.exceptions.JSONDecodeError:
        return "Error: Invalid JSON received from server"

st.title('LANGCHAIN DEMO WITH APIS')
input_text = st.text_input("WRITE ESSAY")
input_text1 = st.text_input("WRITE POEM")

if input_text:
    st.write(get_gemma_response(input_text))
if input_text1:
    st.write(get_phi_response(input_text1))
