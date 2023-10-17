from fastapi import FastAPI, Depends

from app.presentation.user import user_endpoints

app = FastAPI()
app.include_router(user_endpoints.router)


@app.get(path="/health-check", tags=["Operation"])
async def health_check():
    return {"message": "OK"}
