import pytesseract
from pdf2image import convert_from_path
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

KNOWN_STORES = ["Indigo", "Walmart", "Costco", "Target", "Best Buy", "Superstore", "Loblaws", "Metro", "Shoppers"]

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)+'\n'
    return text

def clean_text(text):
    text = re.sub(r"[^A-Za-z0-9\s.,:/-]", "", text)
    text = re.sub(r"\s+", "", text)
    return text.strip()

def extract_store_name(text):
    lines = text.split("\n")
    
    for line in lines[:5]:
        clean_line = clean_text(line)
        
        for store in KNOWN_STORES:
            if store.lower() in clean_line.lower():
                return store
            
        if len(clean_line) > 3 and not re.search(r"\d", clean_line):
            return clean_line
    
    return "Unkown Store"
def extract_date(text):
    date_patterns =[
        r"\b(\d{2,4}[-/.]\d{1,2}[-/.]\d{1,2})\b",
         r"(\d{1,2}/\d{1,2}/\d{2,4})",
    ]
    
    for pattern in date_patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return "Not Found"

def extract_receipt_data(text):
    text = clean_text(text)
    
    total_pattern = r"Total\s*[:$]?\s*([\d,]+\.\d{2})"
    
    # Extract data
    date_value = extract_date(text)
    total_match = re.search(total_pattern, text)
    store_name =extract_store_name(text)
    
    return {
    "Date": date_value,
    "Store": store_name,
    "Total": total_match.group(1) if total_match else "Not Found"
    }
    
pdf_file = "data/sample_receipt.pdf"
text_data = extract_text_from_pdf(pdf_file)
receipt_data = extract_receipt_data(text_data)

print(receipt_data)