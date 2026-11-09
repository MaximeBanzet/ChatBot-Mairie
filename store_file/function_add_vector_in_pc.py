def add_vector(index, document):

    """Fonction qui créer et retourne un vecteur à partir d'un document, et l'ajoute à l'index Pinecone si celui-ci n'existe pas déjà.
    
    :param index: l'index Pinecone dans lequel ajouter le vecteur.
    :param document: le document à transformer en vecteur et à ajouter à l'index.

    :return: None
    """

    result = index.fetch(ids=[document.id])

    if document.id in result.vectors:
        print(f"{document.id} already exists in the index.")
        return

    vector = {
        "id" : document.id,
        "values" : document.embedding,
        "metadata" : {
            "text" : document.text,
            "source" : document.source
        }
    }

    index.upsert(vectors=[vector])
    print(f"{document.id} has been added to the index.")


