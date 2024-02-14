#file_processor.py

import docx
import fitz  # PyMuPDF

def docx_to_text(file_path):
    doc = docx.Document(file_path)
    fullText = [paragraph.text for paragraph in doc.paragraphs]
    return '\n'.join(fullText)

def pdf_to_text(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
