import streamlit as st
from pinecone import Pinecone
from generate_response.search_document import search_document
from generate_response.prompt_builder import prompt_builder
import os
from google import genai
from generate_response.call_llm import call_llm

# Initialisation des variables
pinecone_api_key = os.getenv("PINECONE_API_KEY_PERSO")
pc = Pinecone(api_key=pinecone_api_key)
index = pc.index("rag-chatbot-mairie")
gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)


st.title("ChatBot Mairie")

st.write("Bienvenue sur le ChatBot de la Mairie.")

user_input = st.chat_input("Posez votre question")

if user_input:
    prompt = prompt_builder(query=user_input, index=index, top_k=1)
    response = call_llm(messages=prompt, client=client)
    with st.chat_message("assistant"):
        st.write(response)



