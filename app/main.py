from fastapi import FastAPI
from app.api.view import extract

app = FastAPI()

app.include_router(extract.router)