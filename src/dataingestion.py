from bs4 import BeautifulSoup
import requests
import os

GITHUB_WEB_URL = "https://github.com/fabiopnoronha/credit-fund-bylaws/tree/main/data/raw"
RAW_BASE_URL = "https://raw.githubusercontent.com/fabiopnoronha/credit-fund-bylaws/main/data/raw"
OUTPUT_DIR = "data/raw"

def fetch_file_list_from_github_web():
    """
    Scrape the GitHub webpage to get a list of filenames.
    """
    response = requests.get(GITHUB_WEB_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    file_links = soup.find_all('a', class_='js-navigation-open Link--primary')
    return [link.text for link in file_links if link.text.endswith('.pdf') or link.text.endswith('.docx')]

def download_file_from_github(filename):
    """
    Download a file from GitHub raw link and save it locally.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_url = f"{RAW_BASE_URL}/{filename}"
    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download {filename}. HTTP Status: {response.status_code}")

if __name__ == "__main__":
    # Step 1: Scrape the GitHub webpage for file names
    file_list = fetch_file_list_from_github_web()

    # Step 2: Download each file
    for file in file_list:
        download_file_from_github(file)
