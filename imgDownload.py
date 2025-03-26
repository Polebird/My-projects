import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Set the website URL (Change this to the target website)
url = "https://smvdu.ac.in/"  # Replace with your target URL

# Folder to save images
save_folder = "downloaded_images"
os.makedirs(save_folder, exist_ok=True)

# Fetch the webpage content
response = requests.get(url)
if response.status_code != 200:
    print("Failed to fetch the webpage")
    exit()

# Parse the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Find all image tags
img_tags = soup.find_all("img")

# Download each image
for img in img_tags:
    img_url = img.get("src")
    
    # Make sure the URL is absolute
    img_url = urljoin(url, img_url)
    
    # Get the image name
    img_name = img_url.split("/")[-1]
    
    # Download and save the image
    try:
        img_data = requests.get(img_url).content
        with open(os.path.join(save_folder, img_name), "wb") as img_file:
            img_file.write(img_data)
        print(f"Downloaded: {img_name}")
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")

print("✅ All images downloaded successfully!")
