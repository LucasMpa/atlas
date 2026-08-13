from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO
from uuid import UUID, uuid4

from atlas.infrastructure.storage.local_file_storage import LocalFileStorage


@dataclass(frozen=True)
class StoredDocument:
    id: UUID
    storage_path: Path


class DocumentService:
    def __init__(self, storage: LocalFileStorage) -> None:
        self.storage = storage

    def store_document(self, file_content: BinaryIO) -> StoredDocument:
        document_id = uuid4()
        storage_path = self.storage.save_pdf(document_id, file_content)

        return StoredDocument(id=document_id, storage_path=storage_path)
