from generate_response.search_document import search_document
from pinecone import Pinecone, ServerlessSpec
import os


def prompt_builder(query, index, top_k = 3):

    """ Construit le prompt pour le modèle de génération de réponse en utilisant les documents pertinents.

    :param query: La requête de l'utilisateur.
    :param index: L'index pinecone des documents.
    :param top_k: Le nombre de documents les plus pertinents à inclure dans le prompt (par défaut 3).

    :return: Le prompt construit.
    """

    # Rechercher les documents pertinents dans l'index
    documents = search_document(query, index, top_k)

    context = ""
    compteur_doc = 1
    for doc in documents:
        context += f"""
Document {compteur_doc}
Source: {doc['source']}
Texte: {doc['text']}
"""
        compteur_doc += 1

    prompt = f"""
INSTRUCTIONS: 
Répondez à la requête de l'utilisateur en utilisant les documents pertinents fournis ci-dessous.
Si l'information n'est pas disponible dans les documents, indiquez que vous ne savez pas.

CONTEXTE:
{context}

REQUÊTE:
{query}
"""
    return prompt