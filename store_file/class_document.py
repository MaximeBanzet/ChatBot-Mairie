from .embedding_function import embbeding_text

class DocumentRag:

    """Classe représentant un document pour le RAG (Retrieval-Augmented Generation).

    :param id: L'identifiant unique du document.
    :param text: Le texte du document.
    :param source: La source du document.
    """
    def __init__(self, id, text, source):
        self.id = id
        self.text = text
        self.source = source
        self.embedding = self.get_embedding()

    def get_embedding(self):

        """Retourne l'embedding du texte du document.

        :return: L'embedding du texte.
        """
        return embbeding_text(self.text)