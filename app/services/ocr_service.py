import pytesseract.pytesseract
from pytesseract import image_to_string
from PIL import Image, ImageEnhance
import io
import base64
import logging
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

def preprocess_image(image):
    # Convert to grayscale
    if image.mode != 'L':
        image = image.convert('L')
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    
    return image

async def extract_text_from_base64(base64_image: str):
    try:
        # Remove the data URL prefix if present
        if 'base64,' in base64_image:
            base64_image = base64_image.split('base64,')[1]
        
        # Decode base64 to bytes
        image_bytes = base64.b64decode(base64_image)
        
        # Open and preprocess image
        image = Image.open(io.BytesIO(image_bytes))
        processed_image = preprocess_image(image)
        
        # Extract text with custom configuration
        text = image_to_string(
            processed_image,
            config='--psm 3 --oem 3'  # Page segmentation mode 3 (fully automatic) and LSTM OCR Engine
        )
        
        result = text.strip()
        logger.info(f"Extracted text: {result}")
        
        if not result:
            return "No text detected"
            
        return result
        
    except Exception as e:
        logger.error(f"Error in OCR processing: {str(e)}")
        raise Exception(f"OCR processing failed: {str(e)}")

async def extract_text_from_image(file):
    try:
        content = await file.read()
        image = Image.open(io.BytesIO(content))
        processed_image = preprocess_image(image)
        
        # Extract text with custom configuration
        text = image_to_string(
            processed_image,
            config='--psm 3 --oem 3'  # Page segmentation mode 3 (fully automatic) and LSTM OCR Engine
        )
        
        result = text.strip()
        logger.info(f"Extracted text: {result}")
        
        if not result:
            return "No text detected"
            
        return result
        
    except Exception as e:
        logger.error(f"Error in OCR processing: {str(e)}")
        raise Exception(f"OCR processing failed: {str(e)}")