# https://python.langchain.com/v0.2/docs/introduction/
# https://python.langchain.com/v0.2/docs/tutorial/
# https://python.langchain.com/v0.2/docs/concepts/

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/tutorial/',
    'https://python.langchain.com/v0.2/docs/concepts/'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")
    
threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    
print("All threads have finished fetching content.") 
