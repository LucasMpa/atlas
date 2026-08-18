from uuid import UUID

from pydantic import BaseModel, ConfigDict

from atlas.domain.entities.document import DocumentStatus


class DocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    filename: str
    status: DocumentStatus
