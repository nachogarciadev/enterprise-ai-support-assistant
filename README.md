# Enterprise AI Support Assistant

A modular Python backend for an enterprise AI support assistant, built with FastAPI.

The project aims to provide a reliable foundation for AI-powered question answering over enterprise knowledge sources, with a focus on maintainability, testing, and production-oriented engineering practices.

**Status:** Early development — foundational API with mock responses.

## Tech Stack

- **Python 3.12** — Programming language
- **FastAPI** — REST API framework
- **Pydantic** — Data validation and schemas
- **uv** — Python environment and dependency management
- **pytest & HTTPX** — Automated API testing
- **Ruff** — Linting and code formatting

## Current Features

- REST API with automatic OpenAPI documentation
- Request and response validation using Pydantic
- Modular architecture separating routers, schemas, and services
- Dependency injection through FastAPI
- Mock assistant endpoint
- Automated tests for request validation
- Health and version endpoints

## Project Structure

```text
app/
├── main.py
├── dependencies.py
├── routers/
│   └── assistant.py
├── schemas/
│   └── assistant.py
└── services/
    └── assistant_service.py

tests/
└── test_assistant.py
```

**Architecture responsibilities:**

- `routers/` — HTTP endpoints and request handling
- `schemas/` — Input and output data contracts
- `services/` — Application business logic
- `dependencies.py` — Dependency providers
- `tests/` — Automated API tests

## Getting Started

**Requirements:** Python 3.12 and uv.

Clone the repository:

```bash
git clone https://github.com/nachogarciadev/enterprise-ai-support-assistant.git
cd enterprise-ai-support-assistant
```

Install dependencies:

```bash
uv sync
```

Start the development server:

```bash
uv run uvicorn app.main:app --reload
```

Interactive API documentation:

`http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Application health check |
| GET | `/version` | Application name and version |
| POST | `/assistant/ask` | Submit a question and receive a mock response |

**Example request**

POST `/assistant/ask`

```json
{
  "question": "How can I request annual leave?"
}
```

**Example response**

```json
{
  "answer": "Todavía no hay documentación para: 'How can I request annual leave?'",
  "sources": [],
  "mode": "mock"
}
```

The assistant currently returns predefined mock responses. No LLM or document retrieval integration is implemented yet.

## Testing and Code Quality

Run automated tests:

```bash
uv run python -m pytest -v
```

Check code quality:

```bash
uv run ruff check .
```

Check formatting:

```bash
uv run ruff format --check .
```

## Planned Development

Future development may include:

- LLM integration and structured outputs
- Retrieval-Augmented Generation (RAG)
- Enterprise document ingestion and search
- Retrieval and answer evaluation
- Observability, logging, and error handling
- Docker containerization and deployment
- Authentication and authorization

## Project Goal

This project is being developed as a hands-on exploration of AI Engineering and backend architecture, emphasizing practical implementation, testability, and scalable design.