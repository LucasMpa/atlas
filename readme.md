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
- [ ] Document registration
- [ ] Processing status

---

## Sprint 3 — Indexing Pipeline

- [ ] Text extraction
- [ ] Chunking
- [ ] Embedding generation
- [ ] Vector database storage

---

## Sprint 4 — Intelligent Chat

- [ ] Vector search
- [ ] Context construction
- [ ] LLM integration
- [ ] Document-grounded responses

---

## Sprint 5 — Evolution

- [ ] Conversation history
- [ ] Multiple document support
- [ ] Docker
- [ ] Automated tests
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

### Planned

- PostgreSQL
- pgvector
- OpenAI API
- Ollama
- LangChain
- SQLAlchemy
- Docker
- Pytest
- Ruff

---

# ▶️ Running the Project

Install dependencies:

```bash
uv sync
```

Run the application:

```bash
make run
```

The API will be available at:

```text
http://localhost:8000
```

Interactive API documentation:

```text
http://localhost:8000/docs
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

- Databases
- OpenAI
- Ollama
- PostgreSQL
- FastAPI

Infrastructure is kept behind abstractions so that implementation details can evolve independently from the domain.

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
