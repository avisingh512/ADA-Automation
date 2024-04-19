import requests
from bs4 import BeautifulSoup
import re

def crawl_website(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract relevant information
    headings = soup.find_all(re.compile('^h[1-6]$'))
    links = soup.find_all('a')
    images = soup.find_all('img')
    forms = soup.find_all('form')

    wcag_info = {
        'headings': headings,
        'links': links,
        'images': images,
        'forms': forms,
    }

    return soup, wcag_info