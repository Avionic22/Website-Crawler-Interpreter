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

for img in soup.find_all("img"):
        img_url = img.get("src")
        if img_url:
            file_name = img_url.split("/")[-1]
            response = requests.get(img_url)
            file_content = response.content
            if not os.path.exists('Images'):
                os.makedirs('Images')
            with open(os.path.join('Images', file_name), "wb") as f:
                f.write(file_content)


elements = ['a', 'span', 'h2', 'p', 'h3', 'strong', 'i']
for i in soup.find_all(elements):
    if i.string:
        try:
            i.string.replace_with(tss.google(i.string, from_language='en', to_language='hi'))
        except:
            continue
    else:
        for element in i.contents:
            if element.name is None:  # check if element is a string
                original_text = element.strip()
                if original_text:  # check if element is not empty
                    translated_text = tss.google(original_text, from_language='en', to_language='hi')
                    new_element = BeautifulSoup(translated_text, "lxml").contents[0]
                    element.replace_with(new_element)
with open('output.html', "w", encoding='utf-8') as file:
    file.write(str(soup.prettify()))

