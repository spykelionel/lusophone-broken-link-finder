# This script is specifically for deep linking. It takes a URL and extracts the domain name, 
# then traverses the possible links on this domain to check for a broken link

import csv
import requests
from urllib.parse import urljoin, urlparse, urldefrag
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from collections import deque

def get_response(url):
    """Fetch the HTTP response for a URL, handling errors gracefully."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response
    except RequestException:
        return None

def crawl_site(start_url):
    """Crawl a website starting from a base URL and check all internal links."""
    visited = set()
    queue = deque()
    
    # Normalize the URL and extract domain
    start_url = urldefrag(start_url).url
    parsed_start = urlparse(start_url)
    domain = parsed_start.netloc
    
    if not domain:
        print(f"(Invalid Domain) {start_url}")
        return
    
    queue.append(start_url)
    
    while queue:
        url = queue.popleft()
        
        if url in visited:
            continue
        visited.add(url)
        
        response = get_response(url)
        if not response:
            print(f"(000) {url}")
            continue
        
        status_code = response.status_code
        print(f"({status_code}) {url}")
        
        # Only parse HTML responses for links
        if 'text/html' in response.headers.get('Content-Type', '').lower():
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link['href']
                absolute_url = urljoin(url, href)
                absolute_url = urldefrag(absolute_url).url  # Remove fragment
                parsed_url = urlparse(absolute_url)
                
                # Check if the link is internal and not already visited
                if parsed_url.netloc == domain and absolute_url not in visited:
                    queue.append(absolute_url)

def main():
    """Process each URL in the CSV and initiate crawling."""
    with open('task2.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            if not row:
                continue
            start_url = row[0].strip()
            if start_url:
                crawl_site(start_url)

if __name__ == "__main__":
    main()