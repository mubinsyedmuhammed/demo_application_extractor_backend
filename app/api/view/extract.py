from fastapi import APIRouter, HTTPException
from app.services.ocr_service import extract_text_from_base64
from app.api.models import ImageRequest
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/extract-text")
async def extract_text(request: ImageRequest):
    try:
        logger.info("Processing new image extraction request")
        text = await extract_text_from_base64(request.image)
        
        return JSONResponse(
            content={"extractedText": text},
            status_code=200
        )
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing image: {str(e)}"
        )