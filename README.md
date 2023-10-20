# python-fast-api-example

## Architectures

Python + DDD + [FastAPI](https://github.com/tiangolo/fastapi) + [Alembic (SQLAlchemy)](https://github.com/sqlalchemy/alembic)

## Setup

1. Create a virtual environment.

   ```sh
   python -m venv .venv
   ```

1. Install python modules.

   ```sh
   pip install -r requirements.txt
   ```

1. Migrations to database for executing.

   ```sh
   alembic upgrade head
   ```

## Run and Debug

### Serve

VS Code on select `[Run Serve]` on the Debug start view.

#### Command

```sh
uvicorn main:app --reload
```

### Tests

VS Code on select `[Run Tests]` on the Debug start view.

#### Command

Run all tests.

```sh
pytest -v
```

Run all tests and show coverage.

```sh
pytest -v --cov --cov-branch --cov-report=term-missing
```

## Auto Generating Migrations

#### Command

```sh
alembic revision --autogenerate
```

## Testing API endpoints

You can check the documentation using Swagger UI.

http://localhost:8000/docs#
