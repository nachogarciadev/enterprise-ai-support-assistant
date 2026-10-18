from fastapi import FastAPI
from app.routers import assistant

app = FastAPI(
    title="Enterprise AI Support Assistant",
    version="0.1.0",
)

app.include_router(assistant.router, prefix="/assistant", tags=["assistant"])


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"name": app.title, "version": app.version}
