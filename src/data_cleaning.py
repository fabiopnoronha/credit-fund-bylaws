import os
import pdfplumber
from docx import Document

RAW_DIR = "project/data/raw"         # Directory containing raw files
PROCESSED_DIR = "project/data/processed"  # Directory to save cleaned text files

def create_processed_dir():
    """
    Ensure the processed directory exists.
    """
    os.makedirs(PROCESSED_DIR, exist_ok=True)

def extract_text_from_pdf(filepath):
    """
    Extract text from a PDF file.
    :param filepath: Path to the PDF file.
    :return: Extracted text as a string.
    """
    with pdfplumber.open(filepath) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(filepath):
    """
    Extract text from a DOCX file.
    :param filepath: Path to the DOCX file.
    :return: Extracted text as a string.
    """
    doc = Document(filepath)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)

def clean_text(text):
    """
    Clean extracted text by removing unwanted characters and whitespace.
    :param text: The raw extracted text.
    :return: Cleaned text.
    """
    # Example cleaning: remove extra spaces and newlines
    cleaned_text = " ".join(text.split())
    return cleaned_text

def process_files():
    """
    Process all files in the raw directory.
    """
    create_processed_dir()

    for filename in os.listdir(RAW_DIR):
        filepath = os.path.join(RAW_DIR, filename)
        processed_text = ""

        try:
            if filename.endswith(".pdf"):
                # Extract text from PDFs
                raw_text = extract_text_from_pdf(filepath)
                processed_text = clean_text(raw_text)
            elif filename.endswith(".docx"):
                # Extract text from DOCX files
                raw_text = extract_text_from_docx(filepath)
                processed_text = clean_text(raw_text)
            else:
                print(f"Unsupported file type: {filename}")
                continue

            # Save the cleaned text to a file in the processed directory
            processed_filepath = os.path.join(PROCESSED_DIR, f"{os.path.splitext(filename)[0]}.txt")
            with open(processed_filepath, "w", encoding="utf-8") as f:
                f.write(processed_text)
            print(f"Processed and saved: {processed_filepath}")

        except Exception as e:
            print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    process_files()
