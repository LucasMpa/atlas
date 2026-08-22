import os
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, Request, UploadFile, status

from atlas.api.schemas.document import DocumentResponse
from atlas.infrastructure.database.postgres_document_repository import (
    PostgresDocumentRepository,
)
from atlas.infrastructure.pdf.pdf_parser import PdfParser
from atlas.infrastructure.storage.local_file_storage import LocalFileStorage
from atlas.services.document_service import DocumentService


router = APIRouter(prefix="/documents", tags=["documents"])

database_url = os.environ.get("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL must be set to run the API.")

document_service = DocumentService(
    storage=LocalFileStorage(base_directory=Path("storage/documents")),
    repository=PostgresDocumentRepository(database_url=database_url),
    parser=PdfParser(),
)


@router.post("", response_model=DocumentResponse)
async def create_document(request: Request, file: UploadFile = File(...)):
    """Receive a document."""
    form = await request.form()
    if len(form.getlist("file")) > 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only one file can be uploaded at a time.",
        )

    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Only PDF files are supported.",
        )

    return document_service.store_document(file.filename, file.file)
