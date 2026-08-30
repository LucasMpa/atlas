import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from atlas.api.routes.chat import router as chat_router
from atlas.api.routes.documents import router as documents_router

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Atlas",
    description="Knowledge Base powered by AI",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(documents_router)
app.include_router(chat_router)


@app.get("/")
async def health_check():
    return {
        "status": "running",
    }
