import logging
from typing import BinaryIO
from uuid import uuid4

from atlas.domain.entities.document import Document
from atlas.domain.repositories.document_repository import DocumentRepository
from atlas.infrastructure.chunking.text_chunker import TextChunker
from atlas.infrastructure.pdf.pdf_parser import PdfParser
from atlas.infrastructure.storage.local_file_storage import LocalFileStorage

logger = logging.getLogger(__name__)


class DocumentService:
    def __init__(
        self,
        storage: LocalFileStorage,
        repository: DocumentRepository,
        parser: PdfParser,
        chunker: TextChunker,
    ) -> None:
        self.storage = storage
        self.repository = repository
        self.parser = parser
        self.chunker = chunker

    def store_document(self, filename: str, file_content: BinaryIO) -> Document:
        document_id = uuid4()
        storage_path = self.storage.save_pdf(document_id, file_content)

        document = Document(
            id=document_id,
            filename=filename,
            storage_path=str(storage_path),
        )

        document = self.repository.add(document)

        extracted_text = self.parser.extract_text(storage_path)
        logger.info(
            "Extracted %d characters of text from document %s",
            len(extracted_text),
            document.id,
        )

        chunks = self.chunker.split(extracted_text)
        logger.info("Split document %s into %d chunks", document.id, len(chunks))

        return document
