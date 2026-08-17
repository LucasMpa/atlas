from unittest import TestCase
from uuid import uuid4

from atlas.domain.entities.document import Document, DocumentStatus


class DocumentTestCase(TestCase):
    def test_new_document_starts_with_pending_status_and_utc_timestamps(self) -> None:
        document = Document(
            id=uuid4(),
            filename="manual.pdf",
            storage_path="storage/documents/manual.pdf",
        )

        self.assertEqual(document.status, DocumentStatus.PENDING)
        self.assertEqual(document.created_at.tzinfo, document.updated_at.tzinfo)
        self.assertIsNotNone(document.created_at.tzinfo)
