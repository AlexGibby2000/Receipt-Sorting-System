from PyPDF2 import PdfFileReader

def extract_text_from_pdf(pdf_path):
    reader = PdfFileReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()+"\n"
    return text.strip()

if __name__ == '__main__':
    sample_pdf = 'data/sample_receipt.pdf'
    print(extract_text_from_pdf(sample_pdf))