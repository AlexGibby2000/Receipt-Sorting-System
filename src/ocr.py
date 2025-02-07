import pytesseract
from pdf2image import convert_from_path
import os
import cv2

POPPLER_PATH = r"F:\Code\Dependencies\poppler-24.08.0\Library\bin"
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path,poppler_path=POPPLER_PATH)
    text = ''
    for img in images:
        img_cv = cv2.cvtColor(cv2.imread(img.filename), cv2.COLOR_BGR2RGB)
        text += pytesseract.image_to_string(img_cv)+'\n'
        
    return text

if __name__ == '__main__':
    sample_pdf= "data/sample_receipt.pdf"
    extracted_text = extract_text_from_pdf(sample_pdf)
    print(extracted_text)