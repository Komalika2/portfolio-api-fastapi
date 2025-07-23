# Portfolio API (FastAPI Project)

This is a simple Portfolio API built with FastAPI. It supports adding and reading projects.

## Features

- FastAPI-based REST API
- Pydantic models for validation
- Dockerized
- GitHub Actions CI/CD

## Setup

### Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### Run with Docker

```bash
docker build -t portfolio-api .
docker run -d -p 8000:8000 portfolio-api
```

### Run tests

```bash
pytest
```

## API Endpoints

- `GET /` - Welcome endpoint
- `POST /projects/` - Add project
