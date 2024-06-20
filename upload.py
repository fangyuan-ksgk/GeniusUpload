# URL of the webpage to scrape
url = "https://lexfridman.com/charan-ranganath-transcript"

import requests
from bs4 import BeautifulSoup
from utils import *
# Send a GET request to the webpage
response = requests.get(url)
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    parse_lex_transcript(soup)