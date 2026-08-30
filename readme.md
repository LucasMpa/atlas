<div align="center">

<img src="https://cdn-icons-png.flaticon.com/512/4793/4793147.png" width="120" alt="Atlas Logo">

# Atlas

**AI-Powered Knowledge Base**

An **AI Engineering learning project** focused on understanding, designing and building modern AI applications using **Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), vector databases and intelligent agents**.

The goal is not simply to use AI, but to understand the engineering behind building reliable, maintainable and scalable AI-powered systems.

</div>

---

# 📖 About

Atlas is a knowledge base designed to ingest documents, index their content and answer questions using AI.

The project is being developed incrementally, following an engineering workflow similar to what you might find in a professional software team, with a strong focus on **software architecture, separation of responsibilities, testability and scalability**.

---

# 🎯 Goals

- Build an API using FastAPI.
- Learn the fundamentals of AI Engineering.
- Apply a layered software architecture.
- Understand and implement Retrieval-Augmented Generation (RAG).
- Work with vector databases and semantic search.
- Integrate LLMs through APIs.
- Build an AI application using production-oriented engineering practices.
- Explore the architecture and infrastructure behind modern AI systems.

---

# 🗺️ Roadmap

## Sprint 1 — Project Foundation

- [x] Project initialization with `uv`
- [x] FastAPI configuration
- [x] Initial layered architecture
- [x] Health check

---

## Sprint 2 — Document Upload

- [x] PDF upload
- [x] Local file storage
- [x] Document registration
- [x] Processing status

---

## Sprint 3 — Indexing Pipeline

- [x] Text extraction
- [x] Chunking
- [x] Embedding generation
- [x] Vector database storage

---

## Sprint 4 — Intelligent Chat

- [x] Vector search
- [x] Context construction
- [x] LLM integration
- [x] Document-grounded responses

---

## Sprint 5 — Evolution

- [x] Docker
- [x] Automated tests
- [ ] Conversation history
- [ ] Multiple document support
- [ ] Observability

---

# 🏗️ Project Structure

```text
src/
└── atlas/
    ├── api/
    │   ├── routes/
    │   └── schemas/
    │
    ├── core/
    │
    ├── domain/
    │   ├── entities/
    │   └── repositories/
    │
    ├── infrastructure/
    │   ├── database/
    │   ├── llm/
    │   ├── pdf/
    │   ├── storage/
    │   └── vector_store/
    │
    ├── services/
    │
    ├── __init__.py
    └── main.py

tests/
```

---

# 🧠 Solution Architecture

```text
                 PDF Upload
                     │
                     ▼
              FastAPI API Layer
                     │
                     ▼
              Document Service
                     │
           ┌─────────┴─────────┐
           ▼                   ▼
     Storage Service      Indexer Worker
                               │
                               ▼
                          PDF Parser
                               │
                               ▼
                            Chunking
                               │
                               ▼
                           Embeddings
                               │
                               ▼
                        Vector Database

────────────────────────────────────────────

              User Question
                     │
                     ▼
                Chat Service
                     │
                     ▼
                Vector Search
                     │
                     ▼
             Relevant Chunks
                     │
                     ▼
                    LLM
                     │
                     ▼
               Final Answer
```

---

# 📂 Layered Architecture

| Layer | Responsibility |
| --- | --- |
| **API** | Handles HTTP requests and responses. |
| **Schemas** | Defines API input/output contracts using Pydantic. |
| **Services** | Orchestrates application use cases. |
| **Domain** | Contains business rules and domain entities. |
| **Infrastructure** | Handles external systems such as LLMs, databases, storage, PDF processing and vector stores. |
| **Core** | Contains global application configuration. |

---

# 🚀 Tech Stack

### Current

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic
- uv
- PostgreSQL
- Alembic
- psycopg
- pypdf
- Voyage AI (embeddings)
- pgvector
- Anthropic Claude API (chat/RAG)
- Docker & Docker Compose
- unittest

### Planned

- Local embedding provider (e.g. `sentence-transformers`), as a secondary/fallback option alongside Voyage AI
- Ruff

---

# ▶️ Running the Project

## Environment variables

```bash
cp .env.example .env
```

Fill in `VOYAGE_API_KEY` with a free key from [voyageai.com](https://voyageai.com) and `ANTHROPIC_API_KEY` with a key from [console.anthropic.com](https://console.anthropic.com) (note: this is the developer/API console — separate from a Claude.ai chat subscription, billed independently). The Postgres variables already work out of the box with the Docker setup below.

## Option 1 — Docker Compose (recommended)

```bash
docker compose up -d --build
```

This starts PostgreSQL and the API together. Run the database migrations once:

```bash
make migrate
```

## Option 2 — Local development

Install dependencies:

```bash
uv sync
```

Start PostgreSQL and run the migrations:

```bash
docker compose up -d postgres
make migrate
```

Run the application:

```bash
make run
```

Run the test suite:

```bash
make tests
```

## Endpoints

```text
http://localhost:8000       →  health check
http://localhost:8000/docs  →  interactive API documentation (Swagger)
```

## Usage example

Upload a PDF:

```bash
curl -X POST http://localhost:8000/documents \
  -F "file=@your-document.pdf;type=application/pdf"
```

Ask a question grounded in the documents you've uploaded:

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"userPrompt": "What does the document say about X?"}'
```

---

# 📜 Architectural Principles

Atlas follows a few principles from the beginning of its development.

### Single Responsibility Principle

Each component should have a clear and focused responsibility.

---

### Domain First

Business rules belong to the domain, not to the framework.

---

### Infrastructure Agnostic

The domain should not depend directly on:

- PostgreSQL
- Voyage AI (or any embedding/LLM provider)
- FastAPI

Concrete implementations sit behind `Protocol` interfaces (e.g. `DocumentRepository`, `EmbeddingProvider`), so the application layer only knows the contract, never the specific technology. This is what allows the Postgres repository, or the Voyage embedding provider, to be swapped for a different implementation without touching the service layer.

---

### Incremental Evolution

Features are developed in small, incremental sprints, simulating a professional engineering workflow and making architectural decisions easier to evaluate as the project evolves.

---

# 📚 Learning Goals

Throughout the development of Atlas, the project will explore:

- Software Architecture
- Modern Python
- FastAPI
- Pydantic
- Dependency Injection
- RAG
- Embeddings
- Vector Databases
- Prompt Engineering
- AI Agents
- Observability
- Docker
- Automated Testing
- MLOps fundamentals

---

# 📈 Project Evolution

Atlas started as a Proof of Concept (PoC) for answering questions about PDF documents.

The long-term goal is to evolve it into a platform capable of:

- Analyzing GitHub repositories
- Automatically generating documentation
- Acting as an intelligent Knowledge Base
- Experimenting with different RAG architectures
- Serving as a practical laboratory for AI Engineering studies

The project is intentionally being developed incrementally, with each stage adding a new layer of complexity and engineering concerns.

---

# 📄 License

This project is developed for educational purposes and professional growth.
