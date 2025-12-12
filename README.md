# Basic Commands

1. Install dependencies (if not already done)

```bash
uv sync
```

2. Run the FastAPI app with uvicorn

```bash
uv run uvicorn app.main:app --reload
```

## Project Structure

```
tmnt-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app instance
│   ├── lambda_handler.py    # Lambda entry point with Mangum
│   ├── routers/
│   │   ├── __init__.py
│   │   └── tmnt.py          # API routes
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py       # Pydantic models
│   ├── services/
│   │   ├── __init__.py
│   │   └── business_logic.py
│   └── config.py            # Configuration/settings
├── tests/
│   ├── __init__.py
│   └── test_api.py
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml           # Add mangum dependency
├── README.md
└── template.yaml            # AWS SAM template (or serverless.yml)
```
