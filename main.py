from fastapi import FastAPI, Depends

from domain.usecase import FetchUsersUseCase
from di import inject_fetch_users_usecase

app = FastAPI()


@app.get("/health-check")
async def health_check():
    return {"message": "OK"}


@app.get("/users")
async def get_users(
    fetch_users_usecase: FetchUsersUseCase = Depends(inject_fetch_users_usecase),
):
    return fetch_users_usecase.execute()
