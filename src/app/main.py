from fastapi import FastAPI

from src.app.router import router

app = FastAPI()

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello, my friend!"}
