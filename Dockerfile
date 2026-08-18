FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN addgroup --system app && adduser --system --ingroup app app

COPY pyproject.toml uv.lock readme.md ./
RUN pip install --no-cache-dir uv \
    && uv sync --locked --no-dev --no-install-project

COPY --chown=app:app src ./src
RUN uv sync --locked --no-dev

RUN mkdir -p storage/documents && chown -R app:app storage

USER app

EXPOSE 8000

CMD [".venv/bin/uvicorn", "atlas.main:app", "--host", "0.0.0.0", "--port", "8000"]
