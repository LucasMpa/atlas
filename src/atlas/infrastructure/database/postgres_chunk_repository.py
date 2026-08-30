import numpy as np
from pgvector.psycopg import register_vector
from psycopg import connect

from atlas.domain.entities.chunk import Chunk


class PostgresChunkRepository:
    def __init__(self, database_url: str) -> None:
        self.database_url = database_url

    def add_many(self, chunks: list[Chunk]) -> list[Chunk]:
        if not chunks:
            return []

        query = """
            INSERT INTO chunks (id, document_id, content, chunk_index, embedding, created_at)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        with connect(self.database_url) as connection:
            register_vector(connection)
            with connection.cursor() as cursor:
                cursor.executemany(
                    query,
                    [
                        (
                            chunk.id,
                            chunk.document_id,
                            chunk.content,
                            chunk.chunk_index,
                            chunk.embedding,
                            chunk.created_at,
                        )
                        for chunk in chunks
                    ],
                )

        return chunks

    def find_similar(self, embedding: list[float], limit: int) -> list[Chunk]:
        query = """
            SELECT id, document_id, content, chunk_index, embedding, created_at
            FROM chunks
            ORDER BY embedding <=> %s
            LIMIT %s
        """

        with connect(self.database_url) as connection:
            register_vector(connection)
            with connection.cursor() as cursor:
                cursor.execute(query, (np.array(embedding), limit))
                rows = cursor.fetchall()

        return [
            Chunk(
                id=row[0],
                document_id=row[1],
                content=row[2],
                chunk_index=row[3],
                embedding=row[4].to_list(),
                created_at=row[5],
            )
            for row in rows
        ]
