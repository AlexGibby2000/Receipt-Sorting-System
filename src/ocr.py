import pytesseract
from pdf2image import convert_from_path
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)+'\n'
    return text

def extract_receipt_data(text):
    date_pattern = r"\b(\d{2,4}[-/.]\d{1,2}[-/.]\d{1,2})\b"
    total_pattern = r"Total:\s*\$?([\d,]+\.\d{2})"
    store_pattern = r"(?P<store>[A-za-z\s]+(?:Inc\.|Ltd\.|Store|Supermarket))"
    
    # Extract data
    date_match = re.search(date_pattern, text)
    total_match = re.search(total_pattern, text)
    store_match = re.search(store_pattern, text)
    
    return {
    "Date": date_match.group(1) if date_match else "Not Found",
    "Store": store_match.group("store") if store_match else "Not Found",
    "Total": total_match.group(1) if total_match else "Not Found"
    }
    
pdf_file = "data/sample_receipt.pdf"
text_data = extract_text_from_pdf(pdf_file)
receipt_data = extract_receipt_data(text_data)

print(receipt_data)