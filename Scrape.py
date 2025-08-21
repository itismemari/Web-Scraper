import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from dotenv import dotenv_values

config = dotenv_values(".env")

AUTH = config.AUTH
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

def scrape_website(website):
    print("Lunching Chrome Driver")

    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get(website)
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html

def extract_content_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.body
    if content:
        return str(content)
    return ""

def clean_body_content(content):
    soup = BeautifulSoup(content, 'html.parser')

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    clean_content = soup.get_text(separator="\n")
    clean_content = "\n".join(line.strip() for line in clean_content.splitlines() if line.strip())
    
    return clean_content


def split_dom_content(dom_content , max_lenght = 6000):
    return[
        dom_content[i : i+max_lenght] for i in range( 0 , len(dom_content) , max_lenght)
    ]




