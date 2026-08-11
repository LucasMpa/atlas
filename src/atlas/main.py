from fastapi import FastAPI

app = FastAPI(
    title="Atlas",
    description="Knowledge Base powered by AI",
    version="0.1.0",
)


@app.get("/")
async def health_check():
    return {
        "status": "running",
    }