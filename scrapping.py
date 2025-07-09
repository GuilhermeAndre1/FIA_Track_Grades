from selenium import webdriver
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import time

def scrape_sections_with_tables(url, wait_time=5):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Edge(options=options)
    driver.get(url)
    time.sleep(wait_time)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    content = []
    current_title = ""
    current_desc = ""

    for elem in soup.body.descendants:
        if elem.name in ['h2', 'h3']:
            current_title = elem.get_text(strip=True)
            current_desc = ""
        elif elem.name == 'p':
            text = elem.get_text(strip=True)
            if text:
                current_desc += text + " "
        elif elem.name == 'table' and 'wikitable' in (elem.get('class') or []):
            rows = []
            for row in elem.find_all('tr'):
                cols = row.find_all(['td', 'th'])
                rows.append([c.text.strip() for c in cols])
            content.append({
                'title': current_title,
                'description': current_desc.strip(),
                'table': rows
            })
            current_desc = ""

    return content