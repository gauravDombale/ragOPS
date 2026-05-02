import json
from pathlib import Path

import weaviate
import weaviate.classes as wvc
from openai import OpenAI
from weaviate.classes.config import DataType, Property

from src.config import settings

DATA_PATH = Path("data/sample_docs.json")
COLLECTION_NAME = "Documents"


def load_docs() -> list[dict]:
    with DATA_PATH.open() as f:
        return json.load(f)


def ensure_collection(client: weaviate.WeaviateClient) -> None:
    if client.collections.exists(COLLECTION_NAME):
        return

    client.collections.create(
        name=COLLECTION_NAME,
        vector_config=wvc.config.Configure.Vectors.self_provided(),
        properties=[
            Property(name="content", data_type=DataType.TEXT),
            Property(name="source", data_type=DataType.TEXT),
        ],
    )


def embed_texts(texts: list[str]) -> list[list[float]]:
    oai = OpenAI(api_key=settings.openai_api_key)
    response = oai.embeddings.create(model=settings.embedding_model, input=texts)
    return [item.embedding for item in response.data]


def ingest() -> None:
    docs = load_docs()
    if not docs:
        print("No docs found in data/sample_docs.json")
        return

    client = weaviate.connect_to_local(host=settings.weaviate_host, port=settings.weaviate_port)
    try:
        ensure_collection(client)
        collection = client.collections.get(COLLECTION_NAME)

        texts = [doc["content"] for doc in docs]
        vectors = embed_texts(texts)

        inserted = 0
        for doc, vector in zip(docs, vectors):
            collection.data.insert(
                properties={
                    "content": doc["content"],
                    "source": doc["source"],
                },
                vector=vector,
            )
            inserted += 1

        print(f"Inserted {inserted} documents into '{COLLECTION_NAME}'.")
    finally:
        client.close()


if __name__ == "__main__":
    ingest()
