from fastapi import FastAPI, Depends

from app.presentation import user_endpoints

app = FastAPI()
app.include_router(user_endpoints.router)


@app.get("/health-check")
async def health_check():
    return {"message": "OK"}
