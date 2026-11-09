from store_file.embedding_function import embbeding_text
from pinecone import Pinecone, ServerlessSpec
import os

def search_document (query, index, top_k = 3):
    """
    Recherche les documents les plus pertinents dans l'index en fonction de la requête.

    :param query: La requête de recherche.
    :param index: L'index des documents.
    :param top_k: Le nombre de documents les plus pertinents à retourner (par défaut 3).

    :return: Une liste des documents les plus pertinents.
    """

    # Initialiser la liste des documents pertinents
    documents = []

    # Calcul de l'embedding de la requête
    query_embedding = embbeding_text(query).tolist()

    # Chercher les vecteurs les plus proches dans mon index pinecone
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
        )

    # Ajouter les documents pertinents à la liste
    for match in results['matches']:
        documents.append({'text': match.metadata['text'], 'source': match.metadata['source']})

    return documents

