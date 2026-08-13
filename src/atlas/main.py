from fastapi import FastAPI

from atlas.api.routes.documents import router as documents_router
app = FastAPI(
    title="Atlas",
    description="Knowledge Base powered by AI",
    version="0.1.0",
)

app.include_router(documents_router)


@app.get("/")
async def health_check():
    return {
        "status": "running",
    }
