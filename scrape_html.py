import requests
from bs4 import BeautifulSoup
import os

url = "https://www.dimesia.com/training/174/783/21386/profilemag-home"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Save text
with open('page.html', 'w') as f:
    f.write(response.text)

# Save images
for img in soup.find_all('img'):
    img_url = img['src']
    img_data = requests.get(img_url).content
    with open(os.path.basename(img_url), 'wb') as f:
        f.write(img_data)