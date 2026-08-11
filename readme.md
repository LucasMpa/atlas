<div align="center">

<img src="https://cdn-icons-png.flaticon.com/512/4793/4793147.png" width="120" alt="Atlas Logo">

# Atlas

**Knowledge Base powered by AI**

Projeto de estudos focado em **AI Engineering**, desenvolvido para aprender, na prática, como projetar, construir e evoluir aplicações modernas baseadas em Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), bancos vetoriais e agentes inteligentes.

O objetivo do projeto não é apenas utilizar IA, mas compreender toda a engenharia envolvida na construção de sistemas inteligentes escaláveis.

</div>

---

# 📖 Sobre

O Atlas é uma plataforma capaz de receber documentos, indexar seu conteúdo e responder perguntas utilizando IA.

Este projeto será desenvolvido incrementalmente, simulando o fluxo de desenvolvimento encontrado em equipes de engenharia, com foco em boas práticas de arquitetura de software, separação de responsabilidades e escalabilidade.

---

# 🎯 Objetivos

- Construir uma API utilizando FastAPI.
- Aprender os fundamentos de AI Engineering.
- Implementar uma arquitetura baseada em camadas.
- Compreender o funcionamento do RAG (Retrieval-Augmented Generation).
- Trabalhar com bancos vetoriais.
- Integrar LLMs através de APIs.
- Desenvolver um projeto próximo da realidade encontrada em vagas de AI Engineer.

---

# 🗺️ Roadmap

## Sprint 1 — Estrutura do Projeto

- [x] Inicialização com `uv`
- [x] Configuração do FastAPI
- [x] Estrutura inicial da arquitetura
- [x] Health Check

---

## Sprint 2 — Upload de Documentos

- [ ] Upload de PDF
- [ ] Armazenamento local
- [ ] Cadastro do documento
- [ ] Status de processamento

---

## Sprint 3 — Pipeline de Indexação

- [ ] Extração de texto
- [ ] Chunking
- [ ] Geração de Embeddings
- [ ] Armazenamento no banco vetorial

---

## Sprint 4 — Chat Inteligente

- [ ] Busca vetorial
- [ ] Construção do contexto
- [ ] Integração com LLM
- [ ] Resposta baseada no documento

---

## Sprint 5 — Evolução

- [ ] Histórico de conversas
- [ ] Múltiplos documentos
- [ ] Docker
- [ ] Testes automatizados
- [ ] Observabilidade

---

# 🏗️ Arquitetura

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

# 🧠 Arquitetura da Solução

```text
             Upload PDF
                  │
                  ▼
          FastAPI (API Layer)
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

             Pergunta do Usuário
                     │
                     ▼
               Chat Service
                     │
                     ▼
             Vector Database
                     │
             Chunks Relevantes
                     │
                     ▼
                  LLM
                     │
                     ▼
                Resposta Final
```

---

# 📂 Estrutura em Camadas

| Camada | Responsabilidade |
|---------|------------------|
| **API** | Recebe requisições HTTP e devolve respostas. |
| **Schemas** | Contratos de entrada e saída da API (Pydantic). |
| **Services** | Orquestram os casos de uso da aplicação. |
| **Domain** | Contém as regras de negócio e entidades do sistema. |
| **Infrastructure** | Comunicação com serviços externos (LLM, banco, storage, PDF, banco vetorial). |
| **Core** | Configurações globais da aplicação. |

---

# 🚀 Stack

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic
- uv

## Tecnologias previstas

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

# ▶️ Executando o projeto

Instale as dependências:

```bash
uv sync
```

Execute a aplicação:

```bash
make run
```

A API ficará disponível em:

```
http://localhost:8000
```

Documentação automática:

```
http://localhost:8000/docs
```

---

# 📜 Princípios Arquiteturais

O projeto segue alguns princípios desde sua concepção.

### Single Responsibility Principle

Cada classe possui apenas uma responsabilidade.

---

### Domain First

As regras de negócio pertencem ao domínio, não ao framework.

---

### Infrastructure Agnostic

O domínio não conhece:

- Banco de dados
- OpenAI
- Ollama
- PostgreSQL
- FastAPI

Toda infraestrutura é desacoplada.

---

### Evolução Incremental

Cada funcionalidade será desenvolvida em pequenas sprints, simulando um ambiente profissional.

---

# 📚 Objetivos de Aprendizado

Durante o desenvolvimento do Atlas serão estudados:

- Arquitetura de Software
- FastAPI
- Python Moderno
- Pydantic
- Dependency Injection
- RAG
- Embeddings
- Bancos Vetoriais
- Prompt Engineering
- AI Agents
- Observabilidade
- Docker
- Testes Automatizados
- MLOps (introdução)

---

# 📈 Evolução do Projeto

O Atlas começou como uma Proof of Concept (PoC) para responder perguntas sobre documentos PDF.

A longo prazo, a ideia é evoluir para uma plataforma capaz de:

- analisar repositórios GitHub;
- gerar documentação automaticamente;
- atuar como uma Knowledge Base inteligente;
- servir como laboratório para estudos em AI Engineering.

---

# 📄 Licença

Projeto desenvolvido exclusivamente para fins de estudo e evolução profissional.