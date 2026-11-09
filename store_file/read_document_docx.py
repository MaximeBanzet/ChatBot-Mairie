from pathlib import Path
from docx import Document

def read_word_documents(input_folder="inputs"):
    """
    Lit tous les documents Word (.docx) dans le dossier spécifié et retourne une liste de dictionnaires contenant le nom et le texte de chaque document.
    
    :param input_folder: Le chemin du dossier contenant les fichiers .docx. Par défaut, "inputs".

    :return: Une liste de dictionnaires avec les clés "nom" et "text".
    """
    documents = []

    for file_path in Path(input_folder).glob("*.docx"):

        doc = Document(file_path)
        print(doc.paragraphs)

        text = "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
            if paragraph.text.strip()
        )

        documents.append({
            "nom": file_path.name,
            "text": text
        })

    return documents