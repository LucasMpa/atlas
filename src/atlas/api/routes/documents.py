from pathlib import Path

from fastapi import APIRouter, File, HTTPException, Request, UploadFile, status

from atlas.infrastructure.storage.local_file_storage import LocalFileStorage
from atlas.services.document_service import DocumentService


router = APIRouter(prefix="/documents", tags=["documents"])
document_service = DocumentService(
    storage=LocalFileStorage(base_directory=Path("storage/documents"))
)


@router.post("")
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

    stored_document = document_service.store_document(file.file)

    return {
        "id": str(stored_document.id),
        "filename": file.filename,
    }
