from io import BytesIO
from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock
from uuid import UUID

from atlas.domain.repositories.document_repository import DocumentRepository
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
        self.service = DocumentService(
            storage=self.storage, repository=self.repository, parser=self.parser
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

    def test_store_document_generates_a_unique_id_for_each_file(self) -> None:
        self.storage.save_pdf.side_effect = [
            Path("storage/documents/first.pdf"),
            Path("storage/documents/second.pdf"),
        ]

        first_document = self.service.store_document("first.pdf", BytesIO(b"first"))
        second_document = self.service.store_document("second.pdf", BytesIO(b"second"))

        self.assertNotEqual(first_document.id, second_document.id)
