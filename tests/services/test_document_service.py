from io import BytesIO
from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock
from uuid import UUID

from atlas.domain.repositories.chunk_repository import ChunkRepository
from atlas.domain.repositories.document_repository import DocumentRepository
from atlas.domain.repositories.embedding_provider import EmbeddingProvider
from atlas.infrastructure.chunking.text_chunker import TextChunker
from atlas.infrastructure.pdf.pdf_parser import PdfParser
from atlas.infrastructure.storage.local_file_storage import LocalFileStorage
from atlas.services.document_service import DocumentService


class DocumentServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.storage = Mock(spec=LocalFileStorage)
        self.repository = Mock(spec=DocumentRepository)
        self.repository.add.side_effect = lambda document: document
        self.parser = Mock(spec=PdfParser)
        self.parser.extract_text.return_value = "extracted text"
        self.chunker = Mock(spec=TextChunker)
        self.chunker.split.return_value = ["extracted text"]
        self.embedding_provider = Mock(spec=EmbeddingProvider)
        self.embedding_provider.embed_documents.return_value = [[0.1, 0.2, 0.3]]
        self.chunk_repository = Mock(spec=ChunkRepository)
        self.chunk_repository.add_many.side_effect = lambda chunks: chunks
        self.service = DocumentService(
            storage=self.storage,
            repository=self.repository,
            parser=self.parser,
            chunker=self.chunker,
            embedding_provider=self.embedding_provider,
            chunk_repository=self.chunk_repository,
        )

    def test_store_document_generates_an_id_and_saves_the_file(self) -> None:
        file_content = BytesIO(b"%PDF-1.4")
        storage_path = Path("storage/documents/document.pdf")
        self.storage.save_pdf.return_value = storage_path

        document = self.service.store_document("document.pdf", file_content)

        self.assertIsInstance(document.id, UUID)
        self.assertEqual(document.filename, "document.pdf")
        self.assertEqual(document.storage_path, str(storage_path))
        self.storage.save_pdf.assert_called_once_with(document.id, file_content)

    def test_store_document_persists_the_document_through_the_repository(self) -> None:
        self.storage.save_pdf.return_value = Path("storage/documents/document.pdf")

        document = self.service.store_document("document.pdf", BytesIO(b"%PDF-1.4"))

        self.repository.add.assert_called_once_with(document)

    def test_store_document_extracts_text_from_the_stored_file(self) -> None:
        storage_path = Path("storage/documents/document.pdf")
        self.storage.save_pdf.return_value = storage_path

        self.service.store_document("document.pdf", BytesIO(b"%PDF-1.4"))

        self.parser.extract_text.assert_called_once_with(storage_path)

    def test_store_document_splits_the_extracted_text_into_chunks(self) -> None:
        self.storage.save_pdf.return_value = Path("storage/documents/document.pdf")
        self.parser.extract_text.return_value = "some extracted text"

        self.service.store_document("document.pdf", BytesIO(b"%PDF-1.4"))

        self.chunker.split.assert_called_once_with("some extracted text")

    def test_store_document_generates_embeddings_for_the_chunks(self) -> None:
        self.storage.save_pdf.return_value = Path("storage/documents/document.pdf")
        self.chunker.split.return_value = ["chunk one", "chunk two"]

        self.service.store_document("document.pdf", BytesIO(b"%PDF-1.4"))

        self.embedding_provider.embed_documents.assert_called_once_with(
            ["chunk one", "chunk two"]
        )

    def test_store_document_skips_embeddings_when_there_are_no_chunks(self) -> None:
        self.storage.save_pdf.return_value = Path("storage/documents/document.pdf")
        self.chunker.split.return_value = []

        self.service.store_document("document.pdf", BytesIO(b"%PDF-1.4"))

        self.embedding_provider.embed_documents.assert_not_called()
        self.chunk_repository.add_many.assert_not_called()

    def test_store_document_persists_one_chunk_entity_per_chunk_with_its_embedding(
        self,
    ) -> None:
        self.storage.save_pdf.return_value = Path("storage/documents/document.pdf")
        self.chunker.split.return_value = ["chunk one", "chunk two"]
        self.embedding_provider.embed_documents.return_value = [
            [0.1, 0.2],
            [0.3, 0.4],
        ]

        document = self.service.store_document("document.pdf", BytesIO(b"%PDF-1.4"))

        self.chunk_repository.add_many.assert_called_once()
        (persisted_chunks,), _ = self.chunk_repository.add_many.call_args
        self.assertEqual(len(persisted_chunks), 2)

        self.assertEqual(persisted_chunks[0].document_id, document.id)
        self.assertEqual(persisted_chunks[0].content, "chunk one")
        self.assertEqual(persisted_chunks[0].chunk_index, 0)
        self.assertEqual(persisted_chunks[0].embedding, [0.1, 0.2])

        self.assertEqual(persisted_chunks[1].content, "chunk two")
        self.assertEqual(persisted_chunks[1].chunk_index, 1)
        self.assertEqual(persisted_chunks[1].embedding, [0.3, 0.4])

    def test_store_document_generates_a_unique_id_for_each_file(self) -> None:
        self.storage.save_pdf.side_effect = [
            Path("storage/documents/first.pdf"),
            Path("storage/documents/second.pdf"),
        ]

        first_document = self.service.store_document("first.pdf", BytesIO(b"first"))
        second_document = self.service.store_document("second.pdf", BytesIO(b"second"))

        self.assertNotEqual(first_document.id, second_document.id)
