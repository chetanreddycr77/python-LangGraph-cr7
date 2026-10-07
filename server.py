from fastapi import FastAPI
from route import router

app = FastAPI(
    title="My FastAPI App",
    version="1.0.0"
)

app.include_router(router)


@app.get("/test")
async def root():
    return {
        "message": "Welcome to my FastAPI server"
    }