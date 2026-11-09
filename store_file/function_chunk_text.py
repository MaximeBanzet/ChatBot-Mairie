import unicodedata


def clean_id(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.replace(" ", "_")
    return text

def chunk_text(text, source,chunk_size = 100, overlap = 10):
    
    """
    Fonction qui prend un texte volumineux en entrée et le découpe 
    en plusieurs morceaux de taille 100 avec un chevauchement de 10.and
    Renvoie ensuite une liste de dictionnaires contenant, l'id du chunk, 
    le document source et le texte du chunk.
    """

    words = text.split()
    step = chunk_size - overlap
    compteur_id = 1
    chunks = []

    for i in range(0, len(words), step):
        chunk_words = words[i:i + chunk_size]
        chunk_text = " ".join(chunk_words)
        chunk_id = clean_id(f"id_{source}_{compteur_id}")
        chunks.append({
            "id": chunk_id,
            "source": source,
            "text": chunk_text
        })
        compteur_id += 1

        return chunks




print(chunk_text(text = "1. Demande d'information sur l'entretien de à la voirie\nMadame, Monsieur,\nJe me permets de vous écrire afin d’obtenir des renseignements détaillés sur l’entretien de la voirie dans notre quartier, notamment en ce qui concerne les horaires de passage des équipes techniques et les modalités de ramassage des ordures.\nJe souhaite mieux comprendre le planning d’intervention et les éventuelles perturbations prévues dans la semaine à venir. Pourriez-vous, s’il vous plaît, me communiquer ces informations ou m’indiquer où je pourrais les consulter ?\nDans l’attente de votre réponse, je vous remercie par avance pour votre aide et votre disponibilité.\nCordialement,\nJean Jean", source = "Demande d'information à sur l'entretien de la voirie.docx"))



