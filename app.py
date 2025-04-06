import csv
import requests
from requests.exceptions import RequestException

def get_status_code(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return str(response.status_code)
    except RequestException as e:
        pass

with open('task2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        if not row:  # Skip empty rows
            continue
        url = row[0].strip()
        if url:  # Proceed if URL is not empty
            status_code = get_status_code(url)
            if(status_code is not None):
                print(f"({status_code}) {url}")