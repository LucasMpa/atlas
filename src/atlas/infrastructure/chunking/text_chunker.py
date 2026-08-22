class TextChunker:
    def __init__(self, chunk_size: int = 1000, overlap: int = 200) -> None:
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text: str) -> list[str]:
        if not text:
            return []

        step = self.chunk_size - self.overlap
        chunks = []
        start = 0

        while start < len(text):
            chunks.append(text[start : start + self.chunk_size])
            start += step

        return chunks
