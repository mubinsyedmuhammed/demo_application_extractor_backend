import pytesseract.pytesseract
from pytesseract import image_to_string
from PIL import Image
import io
import base64
import re

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

async def extract_text_from_base64(base64_image: str):
    # Remove the data URL prefix if present
    if 'base64,' in base64_image:
        base64_image = base64_image.split('base64,')[1]
    
    # Decode base64 to bytes
    image_bytes = base64.b64decode(base64_image)
    
    # Open image from bytes
    image = Image.open(io.BytesIO(image_bytes))
    
    # Extract text
    text = image_to_string(image)
    return text.strip()

async def extract_text_from_image(file):
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    text = image_to_string(image)
    return text