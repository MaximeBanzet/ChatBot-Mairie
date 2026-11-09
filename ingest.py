import os
from pinecone import Pinecone, ServerlessSpec
from pathlib import Path
from docx import Document
import store_file
from store_file.class_document import DocumentRag
from store_file.read_document_docx import read_word_documents
from store_file.function_chunk_text import chunk_text
from store_file.function_add_vector_in_pc import add_vector


"""
Script pour créer et accéder à un index Pinecone pour 
le chatbot de la mairie et ingérer tous les documents
nécéssaires pour le RAG.
"""

# Récupérer la clé API Pinecone depuis les variables d'environnement
pinecone_api_key = os.getenv("PINECONE_API_KEY_PERSO")

#Accéder à Pinecone avec la clé API
pc = Pinecone(api_key=pinecone_api_key)

INDEX_NAME = "rag-chatbot-mairie"
#Créer un index Pinecone pour le chatbot de la mairie
if not pc.has_index(INDEX_NAME):
    pc.create_index(
        name = INDEX_NAME,
        dimension = 1024,
        metric = "cosine",
        spec = ServerlessSpec(
            cloud = "aws",
            region = "us-east-1",
        )
    )


#Récupérer l'index Pinecone pour le chatbot de la mairie dans une variable
index = pc.index(INDEX_NAME)

liste_documents_add = read_word_documents(input_folder="inputs")

liste_chunks = []

for document in liste_documents_add:
    chunks = chunk_text(text = document["text"], source = document["nom"])
    liste_chunks.extend(chunks)

print(liste_chunks)


liste_DocumentRag = [DocumentRag(id = chunk["id"], text = chunk["text"], source = chunk["source"]) for chunk in liste_chunks]


for d in liste_DocumentRag:
    add_vector(index=index, document=d)


print(index.describe_index_stats())

