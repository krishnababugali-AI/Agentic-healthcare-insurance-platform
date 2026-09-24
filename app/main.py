from fastapi import FastAPI

app = FastAPI(
    title="Agentic Healthcare Insurance Platform",
    description=(
        "Agentic AI platform for healthcare insurance claims, "
        "prior authorization, benefits verification, policy retrieval, "
        "and appeals."
    ),
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "project": "Agentic Healthcare Insurance Claims & Prior Authorization Platform",
        "status": "active-development",
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}
