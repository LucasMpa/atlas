from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class Chunk:
    id: UUID
    document_id: UUID
    content: str
    chunk_index: int
    embedding: list[float]
    created_at: datetime = field(default_factory=utc_now)
