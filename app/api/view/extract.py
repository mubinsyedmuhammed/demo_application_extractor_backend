from fastapi import APIRouter, HTTPException
from app.services.ocr_service import extract_text_from_base64
from app.api.models import ImageRequest
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/extract-text")  # Removed trailing slash
async def extract_text(request: ImageRequest):
    try:
        text = await extract_text_from_base64(request.image)
        return JSONResponse(
            content={"extractedText": text},
            status_code=200
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))