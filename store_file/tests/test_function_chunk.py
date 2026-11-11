from store_file.function_chunk_text import chunk_text

def test_function_chunk_text():

    # ARRANGE
    text = "Bonjour je suis un document de test"
    source = "test.pdf"

    # ACT
    result = chunk_text(
        text=text,
        source=source,
        chunk_size=4,
        overlap=1
    )

    # ASSERT
    assert len(result) == 3

    assert result[0]["source"] == "test.pdf"
    assert result[0]["text"] == "Bonjour je suis un"

    assert result[1]["text"] == "un document de test"

    assert result[2]["text"] == "test"
