from typing import Protocol

from atlas.domain.entities.chunk import Chunk


class ChunkRepository(Protocol):
    def add_many(self, chunks: list[Chunk]) -> list[Chunk]: ...
