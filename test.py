import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urljoin

def extract_sentences(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract text from visible webpage
    visible_text = soup.get_text()
    # Extract all English sentences
    english_sentences = re.findall(r'\b[A-Z][a-z]*[\.\?!][\s"\']*[A-Z]', visible_text)
    return english_sentences

def process_website(url, max_depth):
    domain = urlparse(url).netloc
    visited_urls = set()
    urls_to_visit = [(url, 0)]
    english_sentences = []
    while urls_to_visit:
        current_url, depth = urls_to_visit.pop(0)
        if current_url in visited_urls:
            continue
        visited_urls.add(current_url)
        if depth > max_depth:
            continue
        try:
            sentences = extract_sentences(current_url)
            english_sentences.extend(sentences)
            response = requests.get(current_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            for link in soup.find_all('a'):
                next_url = link.get('href')
                if next_url and urlparse(next_url).netloc == domain:
                    absolute_url = urljoin(current_url, next_url)
                    urls_to_visit.append((absolute_url, depth + 1))
        except:
            continue
    return english_sentences


url = "https://www.oltrans.bg/en/"
max_depth = 2
english_sentences = process_website(url, max_depth)
print(english_sentences)