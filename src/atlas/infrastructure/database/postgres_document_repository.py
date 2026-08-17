from psycopg import connect

from atlas.domain.entities.document import Document, DocumentStatus


class PostgresDocumentRepository:
    def __init__(self, database_url: str) -> None:
        self.database_url = database_url

    def add(self, document: Document) -> Document:
        query = """
            INSERT INTO documents (
                id,
                filename,
                storage_path,
                status,
                created_at,
                updated_at
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id, filename, storage_path, status, created_at, updated_at
        """

        with connect(self.database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    query,
                    (
                        document.id,
                        document.filename,
                        document.storage_path,
                        document.status.value,
                        document.created_at,
                        document.updated_at,
                    ),
                )
                row = cursor.fetchone()

        return Document(
            id=row[0],
            filename=row[1],
            storage_path=row[2],
            status=DocumentStatus(row[3]),
            created_at=row[4],
            updated_at=row[5],
        )
