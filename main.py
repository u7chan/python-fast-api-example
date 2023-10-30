from fastapi import FastAPI

from app.presentation.auth.login import login_endpoints
from app.presentation.user import user_endpoints


app = FastAPI()
app.include_router(login_endpoints.router)
app.include_router(user_endpoints.router)


@app.get(path="/health-check", tags=["Operation"])
async def health_check():
    return {"message": "OK"}
