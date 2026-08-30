import logging

from atlas.domain.repositories.chunk_repository import ChunkRepository
from atlas.domain.repositories.embedding_provider import EmbeddingProvider
from atlas.domain.repositories.llm_provider import LlmProvider

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You answer questions using only the context provided below. "
    "If the answer is not contained in the context, say you don't know — "
    "do not use any outside knowledge."
)


class ChatService:
    def __init__(
        self,
        embedding_provider: EmbeddingProvider,
        chunk_repository: ChunkRepository,
        llm_provider: LlmProvider,
        top_k: int = 5,
    ) -> None:
        self.embedding_provider = embedding_provider
        self.chunk_repository = chunk_repository
        self.llm_provider = llm_provider
        self.top_k = top_k

    def ask(self, question: str) -> str:
        query_embedding = self.embedding_provider.embed_query(question)
        relevant_chunks = self.chunk_repository.find_similar(
            query_embedding, limit=self.top_k
        )
        logger.info("Found %d relevant chunks for the question", len(relevant_chunks))

        context = "\n\n---\n\n".join(chunk.content for chunk in relevant_chunks)
        user_message = f"Context:\n{context}\n\nQuestion: {question}"

        return self.llm_provider.generate(SYSTEM_PROMPT, user_message)
