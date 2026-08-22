from unittest import TestCase

from atlas.infrastructure.chunking.text_chunker import TextChunker


class TextChunkerTestCase(TestCase):
    def test_split_returns_empty_list_for_empty_text(self) -> None:
        chunker = TextChunker(chunk_size=10, overlap=2)

        self.assertEqual(chunker.split(""), [])

    def test_split_returns_single_chunk_when_text_fits_within_chunk_size(self) -> None:
        chunker = TextChunker(chunk_size=10, overlap=2)

        self.assertEqual(chunker.split("short"), ["short"])

    def test_split_breaks_text_into_overlapping_chunks(self) -> None:
        chunker = TextChunker(chunk_size=10, overlap=2)

        chunks = chunker.split("0123456789abcdefghij")

        self.assertEqual(
            chunks,
            ["0123456789", "89abcdefgh", "ghij"],
        )

    def test_split_consecutive_chunks_overlap_by_the_configured_amount(self) -> None:
        chunker = TextChunker(chunk_size=10, overlap=2)

        chunks = chunker.split("0123456789abcdefghij")

        self.assertEqual(chunks[0][-2:], chunks[1][:2])
