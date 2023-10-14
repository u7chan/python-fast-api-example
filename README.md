# python-fast-api-example

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
uvicorn src.main:app --reload
```

## Auto Generating Migrations

#### run command

```sh
alembic revision --autogenerate
```
