from unittest import TestCase
from unittest.mock import Mock
from uuid import uuid4

from atlas.domain.entities.chunk import Chunk
from atlas.domain.repositories.chunk_repository import ChunkRepository
from atlas.domain.repositories.embedding_provider import EmbeddingProvider
from atlas.domain.repositories.llm_provider import LlmProvider
from atlas.services.chat_service import ChatService


class ChatServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.embedding_provider = Mock(spec=EmbeddingProvider)
        self.embedding_provider.embed_query.return_value = [0.1, 0.2, 0.3]

        self.chunk_repository = Mock(spec=ChunkRepository)
        self.chunk_repository.find_similar.return_value = [
            Chunk(
                id=uuid4(),
                document_id=uuid4(),
                content="chunk one content",
                chunk_index=0,
                embedding=[0.1, 0.2, 0.3],
            ),
            Chunk(
                id=uuid4(),
                document_id=uuid4(),
                content="chunk two content",
                chunk_index=1,
                embedding=[0.4, 0.5, 0.6],
            ),
        ]

        self.llm_provider = Mock(spec=LlmProvider)
        self.llm_provider.generate.return_value = "the answer"

        self.service = ChatService(
            embedding_provider=self.embedding_provider,
            chunk_repository=self.chunk_repository,
            llm_provider=self.llm_provider,
        )

    def test_ask_embeds_the_question_as_a_query(self) -> None:
        self.service.ask("what is this about?")

        self.embedding_provider.embed_query.assert_called_once_with(
            "what is this about?"
        )

    def test_ask_searches_for_similar_chunks_using_the_default_top_k(self) -> None:
        self.service.ask("what is this about?")

        self.chunk_repository.find_similar.assert_called_once_with(
            [0.1, 0.2, 0.3], limit=5
        )

    def test_ask_generates_an_answer_using_the_retrieved_chunks_as_context(
        self,
    ) -> None:
        answer = self.service.ask("what is this about?")

        self.llm_provider.generate.assert_called_once()
        _, user_message = self.llm_provider.generate.call_args[0]
        self.assertIn("chunk one content", user_message)
        self.assertIn("chunk two content", user_message)
        self.assertIn("what is this about?", user_message)
        self.assertEqual(answer, "the answer")

    def test_ask_respects_a_custom_top_k(self) -> None:
        service = ChatService(
            embedding_provider=self.embedding_provider,
            chunk_repository=self.chunk_repository,
            llm_provider=self.llm_provider,
            top_k=2,
        )

        service.ask("what is this about?")

        self.chunk_repository.find_similar.assert_called_once_with(
            [0.1, 0.2, 0.3], limit=2
        )
