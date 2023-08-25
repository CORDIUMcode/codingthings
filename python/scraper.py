
import os
import requests
from bs4 import BeautifulSoup

def create_extract_folder():
    # Desktop directory path for Windows
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    extract_folder_path = os.path.join(desktop_path, 'Extract')

    # Create the 'Extract' folder if it doesn't exist
    if not os.path.exists(extract_folder_path):
        os.makedirs(extract_folder_path)

    return extract_folder_path

def scrape_website(url):
    # Fetch website content using requests
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to fetch the website. Status code: {response.status_code}")
        return None

def extract_data_to_folder(html_content, extract_folder_path):
    if not html_content:
        print("No content to extract.")
        return

    # Parse the website content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')

    # Extract data here
    # For example, let's extract all the links from the website
    links = soup.find_all('a')

    # Save the links to a text file in the 'Extract' folder
    with open(os.path.join(extract_folder_path, 'extracted_links.txt'), 'w', encoding='utf-8') as file:
        for link in links:
            file.write(link.get('href') + '\n')

if __name__ == "__main__":
    # URL of the website you want to scrape
    target_url = "https://www.cordiummusic.com/"

    # Step 1: Create the 'Extract' folder
    extract_folder_path = create_extract_folder()

    # Step 2: Scrape the website
    website_content = scrape_website(target_url)

    # Step 3: Extract the data to the 'Extract' folder
    extract_data_to_folder(website_content, extract_folder_path)

    print("Extraction complete. Check the 'Extract' folder on your desktop.")
