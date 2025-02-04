import os
from src.ocr import extract_text_from_pdf
from src.file_manager import move_receipt

DATA_FOLDER = "data"

def process_receipts():
    for file in os.listdir(DATA_FOLDER):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(DATA_FOLDER, file)
            text = extract_text_from_pdf(pdf_path)
            move_receipt(pdf_path, text)
            print(f"Processed: {file}")
    
if __name__ == '__main__':
    process_receipts()