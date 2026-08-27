import logging
from typing import BinaryIO
from uuid import uuid4

from atlas.domain.entities.chunk import Chunk
from atlas.domain.entities.document import Document
from atlas.domain.repositories.chunk_repository import ChunkRepository
from atlas.domain.repositories.document_repository import DocumentRepository
from atlas.domain.repositories.embedding_provider import EmbeddingProvider
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
        embedding_provider: EmbeddingProvider,
        chunk_repository: ChunkRepository,
    ) -> None:
        self.storage = storage
        self.repository = repository
        self.parser = parser
        self.chunker = chunker
        self.embedding_provider = embedding_provider
        self.chunk_repository = chunk_repository

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

        if chunks:
            embeddings = self.embedding_provider.embed_documents(chunks)
            logger.info(
                "Generated %d embeddings for document %s", len(embeddings), document.id
            )

            chunk_entities = [
                Chunk(
                    id=uuid4(),
                    document_id=document.id,
                    content=content,
                    chunk_index=index,
                    embedding=embedding,
                )
                for index, (content, embedding) in enumerate(zip(chunks, embeddings))
            ]
            self.chunk_repository.add_many(chunk_entities)
            logger.info(
                "Persisted %d chunks for document %s", len(chunk_entities), document.id
            )

        return document
