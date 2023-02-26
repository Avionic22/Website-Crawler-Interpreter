import translators.server as tss
import translators as ts
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import os

web_url1 = 'https://www.classcentral.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'}

html_text = requests.get(web_url1, headers=headers).text
soup = BeautifulSoup(html_text, "lxml")

for script in soup.find_all("script"):
    script_url = script.get("src")
    print(script_url)
    if script_url:
        file_name = script_url.split("/")[-1]
        try:
            response = requests.get(script_url)
        except:
            print('invalid url')
            continue
        file_content = response.content
        if not os.path.exists('Scripts'):
            os.mkdir('Scripts')
        with open(os.path.join('Scripts', file_name), "wb") as f:
            f.write(file_content)