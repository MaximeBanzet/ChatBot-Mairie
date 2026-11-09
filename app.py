import streamlit as st
from pinecone import Pinecone
from generate_response.search_document import search_document
from generate_response.prompt_builder import prompt_builder
import os

# Initialisation des variables
pinecone_api_key = os.getenv("PINECONE_API_KEY_PERSO")
pc = Pinecone(api_key=pinecone_api_key)
index = pc.index("rag-chatbot-mairie")
sys_messages = {"role": "system", "content": "Vous êtes un assistant pour la Mairie, ton rôle est de répondre aux différents utilisateurs à partir des informations qui te sont données. Si tu n'as pas la réponse à une question, n'invente rien et indique que vous ne savez pas."}


st.title("ChatBot Mairie")

st.write("Bienvenue sur le ChatBot de la Mairie.")

user_input = st.chat_input("Posez votre question")

if user_input:
    prompt = prompt_builder(query=user_input, index=index, top_k=1)
    with st.chat_message("assistant"):
        st.write(prompt)

