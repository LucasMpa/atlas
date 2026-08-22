from pathlib import Path

from pypdf import PdfReader


class PdfParser:
    def extract_text(self, file_path: Path) -> str:
        reader = PdfReader(file_path)
        return "\n".join(page.extract_text() for page in reader.pages)
