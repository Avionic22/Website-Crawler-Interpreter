import translators.server as tss
import translators as ts
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

web_url1 = 'https://www.classcentral.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'}


class WebCrawler:

    def __init__(self, web_url):
        self.web_url = web_url

    def get_all_links(self):
        html_text = requests.get(self.web_url, headers=headers).text
        soup = BeautifulSoup(html_text, "lxml")
        urls = [new_url.get('href') for new_url in soup.find('main').find_all('a', href=True)]
        links = [urljoin(self.web_url, url) for url in urls]
        return links

    def translate_all_page(self, html):
        elements = ['a', 'span', 'h2', 'p', 'h3', 'strong', 'i']
        html_text = requests.get(self.web_url, headers=headers).text
        soup = BeautifulSoup(html_text, "lxml")
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
                            new_element = BeautifulSoup(translated_text, "lxml").contents
                            if new_element:
                                element.replace_with(new_element[0])
        with open(html, "w", encoding='utf-8') as file:
            file.write(str(soup.prettify()))


web_crawler = WebCrawler(web_url1)
linkss = web_crawler.get_all_links()
x = 0
for link in linkss[:2]:
    WebCrawler(link).translate_all_page("output{}.html".format(x))
    x += 1

