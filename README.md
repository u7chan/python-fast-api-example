# python-fast-api-example

## setup

1. create venv

   ```sh
   python -m venv .venv
   ```

1. install

   ```sh
   pip install -r requirements.txt
   ```

1. migrations to database for executing

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
