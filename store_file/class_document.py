from .embedding_function import embbeding_text

class DocumentRag:
    def __init__(self, id, text, source):
        self.id = id
        self.text = text
        self.source = source
        self.embedding = self.get_embedding()

    def get_embedding(self):
        return embbeding_text(self.text)