import os
import shutil
import re
from datetime import datetime

SORTED_FOLDER= "sorted_receipts"

def extract_date(text):
    
    date_patterns = [
        r"(\d{4}/\d{2}/\d{2})", #YYYY/MM/DD
        r"(\d{2}/\d{2}/\d{4})", #MM/DD/YYYY
        r"(\d{2}-\d{2}-\d{4})", #MM-DD-YYYY
    ]
    
    for pattern in date_patterns:
        match = re.search(pattern, text)
        if match:
            try:
                return datetime.strptime(match.group(0), "%m/%d/%Y").strftime("%Y-%m-%d")
            except ValueError:
                continue
    return "Unknown"

def extract_store_name(text):
    words = text.split()
    for word in words:
        if word.isalpha() and word.isupper():
            return word
    return "Unknown_Store"

def move_receipt(pdf_path, text):
    date = extract_date(text)
    store = extract_store_name(text)
    target_folder = os.path.join(SORTED_FOLDER, date, store)
    
    os.makedirs(target_folder, exist_ok=True)
    shutil.move(pdf_path, os.path.join(target_folder, os.path.basename(pdf_path)))
    
if __name__ == '__main__':
    sample_text= "Receipt from: WALMART on 02/15/2023. Total: $100.00"
    print(extract_date(sample_text))
    print(extract_store_name(sample_text))
            