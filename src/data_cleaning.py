# src/data_cleaning.py

import re

def basic_cleaning(text: str) -> str:
    """
    Perform basic text cleaning, e.g.:
    - Removing excessive whitespace
    - Removing non-ASCII characters (optional, if needed)
    - Ensuring consistent newlines
    """
    # If you want to remove non-ASCII:
    # text = text.encode("ascii", "ignore").decode()
    
    # Convert multiple whitespaces to single space
    text = re.sub(r"\s+", " ", text)
    
    # Trim
    text = text.strip()
    return text

