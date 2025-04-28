from fastapi import APIRouter, UploadFile, File
from app.services.ocr_service import extract_text_from_image

router = APIRouter()

@router.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    text = await extract_text_from_image(file)
    return {"extracted text": text}