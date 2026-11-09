def call_llm(messages, client):

    """Appelle le modèle LLM avec les messages fournis et retourne la réponse générée.

    :param messages: Liste de messages à envoyer au modèle LLM. Chaque message est un dictionnaire avec les clés "role" et "content".
    :param client: Le client Gemini API utilisé pour appeler le modèle LLM.
    :return: La réponse générée par le modèle LLM.
    """

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=messages,
    )
    return interaction.output_text


    