from io import BytesIO
from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock
from uuid import UUID

from atlas.infrastructure.storage.local_file_storage import LocalFileStorage
from atlas.services.document_service import DocumentService


class DocumentServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.storage = Mock(spec=LocalFileStorage)
        self.service = DocumentService(storage=self.storage)

    def test_store_document_generates_an_id_and_saves_the_file(self) -> None:
        file_content = BytesIO(b"%PDF-1.4")
        storage_path = Path("storage/documents/document.pdf")
        self.storage.save_pdf.return_value = storage_path

        stored_document = self.service.store_document(file_content)

        self.assertIsInstance(stored_document.id, UUID)
        self.assertEqual(stored_document.storage_path, storage_path)
        self.storage.save_pdf.assert_called_once_with(stored_document.id, file_content)

    def test_store_document_generates_a_unique_id_for_each_file(self) -> None:
        self.storage.save_pdf.side_effect = [
            Path("storage/documents/first.pdf"),
            Path("storage/documents/second.pdf"),
        ]

        first_document = self.service.store_document(BytesIO(b"first"))
        second_document = self.service.store_document(BytesIO(b"second"))

        self.assertNotEqual(first_document.id, second_document.id)
