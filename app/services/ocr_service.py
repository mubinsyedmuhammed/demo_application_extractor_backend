import pytesseract.pytesseract
from pytesseract import image_to_string
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

async def extract_text_from_image(file):
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    text = image_to_string(image)
    return text