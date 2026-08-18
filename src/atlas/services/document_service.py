from typing import BinaryIO
from uuid import uuid4

from atlas.domain.entities.document import Document
from atlas.domain.repositories.document_repository import DocumentRepository
from atlas.infrastructure.storage.local_file_storage import LocalFileStorage


class DocumentService:
    def __init__(self, storage: LocalFileStorage, repository: DocumentRepository) -> None:
        self.storage = storage
        self.repository = repository

    def store_document(self, filename: str, file_content: BinaryIO) -> Document:
        document_id = uuid4()
        storage_path = self.storage.save_pdf(document_id, file_content)

        document = Document(
            id=document_id,
            filename=filename,
            storage_path=str(storage_path),
        )

        return self.repository.add(document)
