from typing import Protocol

from atlas.domain.entities.document import Document


class DocumentRepository(Protocol):
    def add(self, document: Document) -> Document: ...
