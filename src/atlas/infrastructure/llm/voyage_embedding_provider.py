import voyageai


class VoyageEmbeddingProvider:
    def __init__(self, api_key: str, model: str = "voyage-4") -> None:
        self.client = voyageai.Client(api_key=api_key)
        self.model = model

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        result = self.client.embed(texts, model=self.model, input_type="document")
        return result.embeddings
