# src/data_ingestion.py

import os
import pdfplumber
import docx2txt

def read_pdf(file_path: str) -> str:
    """Reads a PDF file and returns the extracted text."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def read_docx(file_path: str) -> str:
    """Reads a DOCX file and returns the extracted text."""
    text = docx2txt.process(file_path)
    return text

def load_bylaws(input_dir: str = "data/raw") -> list:
    """
    Loads all bylaw files (PDF or DOCX) from the input directory.
    Returns a list of tuples: (filename, raw_text).
    """
    all_documents = []
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        if not os.path.isfile(file_path):
            continue  # Skip if it's a folder or something else
        
        ext = filename.lower().rsplit(".", 1)[-1]
        
        if ext == "pdf":
            doc_text = read_pdf(file_path)
        elif ext == "docx":
            doc_text = read_docx(file_path)
        else:
            # Skip if it's not PDF or DOCX
            continue
        
        all_documents.append((filename, doc_text))
    
    return all_documents

if __name__ == "__main__":
    docs = load_bylaws("data/raw")
    print(f"Loaded {len(docs)} bylaw files.")
 
