from fastapi import FastAPI

app = FastAPI(
    title="Comic Users API",
    description="API that handles user data for comics store",
    version="0.1.0",
)


@app.get("/")
async def home_page():
    """Homepage"""

    return {"message": "Welcome to the Comic Users API"}