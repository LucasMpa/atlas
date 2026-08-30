import os

from fastapi import APIRouter

from atlas.api.schemas.chat import ChatRequest, ChatResponse
from atlas.infrastructure.database.postgres_chunk_repository import (
    PostgresChunkRepository,
)
from atlas.infrastructure.llm.claude_llm_provider import ClaudeLlmProvider
from atlas.infrastructure.llm.voyage_embedding_provider import VoyageEmbeddingProvider
from atlas.services.chat_service import ChatService


router = APIRouter(prefix="/chat", tags=["chat"])

database_url = os.environ.get("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL must be set to run the API.")

voyage_api_key = os.environ.get("VOYAGE_API_KEY")
if not voyage_api_key:
    raise RuntimeError("VOYAGE_API_KEY must be set to run the API.")

anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
if not anthropic_api_key:
    raise RuntimeError("ANTHROPIC_API_KEY must be set to run the API.")

chat_service = ChatService(
    embedding_provider=VoyageEmbeddingProvider(api_key=voyage_api_key),
    chunk_repository=PostgresChunkRepository(database_url=database_url),
    llm_provider=ClaudeLlmProvider(api_key=anthropic_api_key),
)


@router.post("", response_model=ChatResponse)
async def create_chat(request: ChatRequest):
    """Answer a question grounded in the indexed documents."""
    answer = chat_service.ask(request.user_prompt)
    return ChatResponse(answer=answer)
