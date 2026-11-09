from FlagEmbedding import BGEM3FlagModel


# Créer la fonction d'embedding pour un texte donné
def embbeding_text(texte):

    """Fonction qui prend un texte en entrée et retourne son vecteur d'embedding dense de dimension 1024 avec le model BAAI/bge-m3 opensource d'HuggingFace.

    :param texte: Le texte à encoder en vecteur d'embedding.
    :return: Le vecteur d'embedding dense de dimension 1024.
    """

    model = BGEM3FlagModel("BAAI/bge-m3")
    result = model.encode([texte])
    return result["dense_vecs"][0]


texte = "hello mon nom est ilyana et ce soir je vais manger au restaurant"
print(embbeding_text(texte))
