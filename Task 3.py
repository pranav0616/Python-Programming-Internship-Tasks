import requests
from bs4 import BeautifulSoup
import sys

url = 'https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial/?ref=home-articlecards'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    page_text = soup.get_text()

    links = [a['href'] for a in soup.find_all('a', href=True)]
    images = [img['src'] for img in soup.find_all('img', src=True)]

    sys.stdout.buffer.write("Page text: \n".encode('utf-8'))
    sys.stdout.buffer.write(page_text.encode('utf-8'))

    print("\nLinks: ")
    for link in links:
        print(link)

    print("\nImages: ")
    for image in images:
        print(image)

else:
    print(f"Failed to retrieve web page. Status code: {response.status_code}")
