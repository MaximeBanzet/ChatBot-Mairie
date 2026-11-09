from transformers import AutoProcessor, AutoModelForMultimodalLM

def call_llm(messages):

    """Appelle le modèle LLM avec les messages fournis et retourne la réponse générée.

    :param messages: Liste de messages à envoyer au modèle LLM. Chaque message est un dictionnaire avec les clés "role" et "content".
    :return: La réponse générée par le modèle LLM.
    """
    MODEL_ID = "google/gemma-4-31B-it"

    # Load model
    processor = AutoProcessor.from_pretrained(MODEL_ID)
    model = AutoModelForMultimodalLM.from_pretrained(
        MODEL_ID,
        dtype = "auto",
        device_map="auto"
        )

    # Process input

    inputs = processor.apply_chat_template(
        messages,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
        add_generation_prompt=True,
        enable_thinking=False
        ).to(model.device)

    input_len = inputs["input_ids"].shape[-1]

    # Generate output
    outputs = model.generate(**inputs, max_new_tokens=1024)
    response = processor.decode(outputs[0][input_len:], skip_special_tokens=False)

    return processor.parse_response(response, prefix=inputs["input_ids"])

messages = [
    {"role" : "user", "content": "Quelle est la capitale de la France ?"}
]

print(call_llm(messages))



    