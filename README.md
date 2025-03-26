# URL Status Checker & Deep Link Crawler

A Python toolset to check HTTP status codes of URLs from a CSV file and crawl websites to find broken internal links.

## Features

1. **URL Status Checker**:

   - Reads URLs from a CSV file and prints their HTTP status codes.
   - Handles network errors, timeouts, and invalid URLs gracefully.

2. **Deep Link Crawler**:
   - Crawls a website starting from a base URL.
   - Traverses all internal links (same domain) using BFS.
   - Reports broken links (e.g., 404, 500) and network errors.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Virtual Environment](#virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Usage](#usage)
  - [1. URL Status Checker](#1-url-status-checker)
  - [2. Deep Link Crawler](#2-deep-link-crawler)
- [Common Issues](#common-issues)
- [Contributing](#contributing)
- [License](#license)

---

## Prerequisites

- Python 3.6+
- `pip` (Python package installer)
- For the Deep Link Crawler:
  - HTML parsing requires `beautifulsoup4` and `lxml`.

---

## Setup

### Virtual Environment

Create and activate a virtual environment to isolate dependencies:

#### **macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

#### **Windows (PowerShell)**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

1. Create a `requirements.txt` file with:

   ```text
   requests==2.26.0
   beautifulsoup4==4.10.0
   lxml==4.6.3
   ```

2. Install packages:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. URL Status Checker

#### Input File Format

Create a CSV file (e.g., `urls.csv`) with a header `urls` followed by URLs:

```csv
urls
http://example.com
http://nonexistent-site-12345.com
```

#### Run the Script

```bash
python url_status_checker.py
```

#### Output

```text
(200) http://example.com
(000) http://nonexistent-site-12345.com
```

---

### 2. Deep Link Crawler

#### Input File Format

Create a CSV file (e.g., `sites.csv`) with base URLs to crawl:

```csv
urls
https://example.com
http://broken-links-test-site.com
```

#### Run the Script

```bash
python deep_link_crawler.py
```

#### Output

```text
(200) https://example.com
(404) https://example.com/dead-link
(503) https://example.com/service-down
```

---

## Common Issues

1. **Timeouts/Connection Errors**:

   Increase the `timeout` value in `get_response()` (default: 10 seconds).

2. **Robots.txt Restrictions**:

   Some sites block crawlers. Add a `robots.txt` checker if needed.

3. **Rate Limiting**:

   Add a delay between requests to avoid being blocked:

   ```python
   import time
   time.sleep(1)  # Add this in the crawl loop
   ```

4. **SSL Errors**:

   Disable SSL verification (not recommended for production):

   ```python
   response = requests.get(url, verify=False)
   ```

---

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/new-feature`.
3. Commit changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.

---

### Notes for Users

- **Virtual Environment**: Always activate the virtual environment before running scripts.
- **CSV Format**: Ensure the CSV has a header row labeled `urls`.
- **Output**: Broken links are flagged with non-200 status codes (e.g., `404`, `500`). Network errors show `000`.
