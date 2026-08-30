from unittest import TestCase
from uuid import uuid4

from atlas.domain.entities.chunk import Chunk


class ChunkTestCase(TestCase):
    def test_new_chunk_has_a_utc_created_at_timestamp(self) -> None:
        chunk = Chunk(
            id=uuid4(),
            document_id=uuid4(),
            content="some chunk text",
            chunk_index=0,
            embedding=[0.1, 0.2, 0.3],
        )

        self.assertIsNotNone(chunk.created_at.tzinfo)
