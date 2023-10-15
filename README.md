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

#### for VSCode

- VS Code on select [Run] on the Debug start view.

#### for Command

```sh
uvicorn main:app --reload
```

## Auto Generating Migrations

#### run command

```sh
alembic revision --autogenerate
```

## Testing API endpoints

You can check the documentation using Swagger UI.

http://localhost:8000/docs#
