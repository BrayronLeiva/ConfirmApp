
from fastapi import FastAPI
from app.webservices.routes import router as api_router

app = FastAPI(title="Confirm App API")
app.include_router(api_router)

