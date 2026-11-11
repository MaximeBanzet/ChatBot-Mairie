from unittest.mock import MagicMock
from types import SimpleNamespace

from store_file.function_add_vector_in_pc import add_vector


def test_add_vector_when_document_doesnt_exist():
    index = MagicMock()

    document = SimpleNamespace(
        id="doc1", 
        embedding=[0.1, 0.2, 0.3], 
        text = "Ceci est le document 1", 
        source = "doc.pdf"
        )

    index.fetch.return_value.vectors = {}

    result = add_vector(index, document)

    index.fetch.assert_called_once_with(ids=["doc1"])

    index.upsert.assert_called_once_with(
        vectors=[
            {
                "id": "doc1",
                "values": [0.1, 0.2, 0.3],
                "metadata": {
                    "text": "Ceci est le document 1",
                    "source": "doc.pdf"
                }
            }
        ]
    )

    assert result is None


def test_add_vector_when_document_exists():
    index = MagicMock()

    document = SimpleNamespace(
        id="doc1",
        embedding=[0.1, 0.2, 0.3],
        text="Ceci est le document 1",
        source="doc.pdf"
    )

    index.fetch.return_value.vectors = {
        "doc1": {}
    }

    result = add_vector(index, document)

    index.fetch.assert_called_once_with(ids=["doc1"])

    index.upsert.assert_not_called()

    assert result is None