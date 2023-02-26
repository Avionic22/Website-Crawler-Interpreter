import translators.server as tss
import translators as ts
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

web_url1 = 'https://www.classcentral.com/login'
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

downloaded_links = [
    'https://www.classcentral.com/institution/amazon',
    'https://www.classcentral.com/institution/smithsonian',
    'https://www.classcentral.com/report/author/manoel/',
    'https://www.classcentral.com/university/mit',
    'https://www.classcentral.com/provider/swayam',
    'https://www.classcentral.com/report/',
    'https://www.classcentral.com/provider/futurelearn',
    'https://www.classcentral.com/report/most-popular-online-courses/',
    'https://www.classcentral.com/provider/udemy',
    'https://www.classcentral.com/rankings',
    'https://www.classcentral.com/university/stanford',
    'https://www.classcentral.com/report/online-learning-deals/',
    'https://www.classcentral.com/help/moocs',
    'https://www.classcentral.com/subject/personal-development',
    'https://www.classcentral.com/course/mindfulness-wellbeing-performance-3714',
    'https://www.classcentral.com/report/author/pat-bowden/',
    'https://www.classcentral.com/collection/sustainability-online-courses',
    'https://www.classcentral.com/subject/cs',
    'https://www.classcentral.com/report/best-free-prolog-courses/',
    'https://www.classcentral.com/university/harvard',
    'https://www.classcentral.com/report/author/dhawal/',
    'https://www.classcentral.com/report/best-ocaml-courses/',
    'https://www.classcentral.com/report/mooc-based-masters-degree/',
    'https://www.classcentral.com/report/udemy-new-ceo/',
    'https://www.classcentral.com/provider/skillshare',
    'https://www.classcentral.com/collection/top-free-online-courses',
    'https://www.classcentral.com/report/category/best-courses/',
    'https://www.classcentral.com/university/cornell',
    'https://www.classcentral.com/university/rice',
    'https://www.classcentral.com/university/purdue',
    'https://www.classcentral.com/provider/edx',
    'https://www.classcentral.com/report/india-online-degrees/',
    'https://www.classcentral.com/university/duke',
    'https://www.classcentral.com/report/best-davinci-resolve-courses/',
    'https://www.classcentral.com/university/columbia',
    'https://www.classcentral.com/course/python-statistics-financial-analysis-12648',
    'https://www.classcentral.com/subjects',
    'https://www.classcentral.com/report/thinkific-layoffs/',
    'https://www.classcentral.com/report/free-google-certifications/',
    'https://www.classcentral.com/institution/british-council',
    'https://www.classcentral.com/collections',
    'https://www.classcentral.com/report/domestika-layoffs/',
    'https://www.classcentral.com/providers',
    'https://www.classcentral.com/report/best-japanese-courses/',
    'https://www.classcentral.com/university/iitm',
    'https://www.classcentral.com/institution/microsoft',
    'https://www.classcentral.com/university/edinburgh',
    'https://www.classcentral.com/institution/google',
    'https://www.classcentral.com/collection/ivy-league-moocs',
    'https://www.classcentral.com/course/teaching-young-learners-online-20139',
    'https://www.classcentral.com/report/harvard-cs50-guide/',
    'https://www.classcentral.com/course/swayam-functional-foods-and-nutraceuticals-14069',
    'https://www.classcentral.com/institution/ibm',
    'https://www.classcentral.com/provider/linkedin-learning',
    'https://www.classcentral.com/report/free-certificates/',
    'https://www.classcentral.com/subject/it-certifications',
    'https://www.classcentral.com/report/udemy-top-courses/',
    'https://www.classcentral.com/report/list-of-mooc-based-microcredentials/',
    'https://www.classcentral.com/subject/business',
    'https://www.classcentral.com/collection/top-free-online-courses',
    'https://www.classcentral.com/subject/programming-and-software-development',
    'https://www.classcentral.com/universities',
    'https://www.classcentral.com/course/edx-circular-fashion-design-science-and-value-in-a-sustainable-clothing-industry-17080',
    'https://www.classcentral.com/report/author/ruima/',
    'https://www.classcentral.com/report/udemy-by-the-numbers/',
    'https://www.classcentral.com/university/penn',
    'https://www.classcentral.com/report/coursera-free-online-courses/',
    'https://www.classcentral.com/course/modelthinking-317',
    'https://www.classcentral.com/provider/coursera',
    'https://www.classcentral.com/course/modpo-356',
    'https://www.classcentral.com/university/umich',
    'https://www.classcentral.com/report/best-resume-writing-courses/',
    'https://www.classcentral.com/subject/python',
    'https://www.classcentral.com/report/futurelearn-expands-paywall/',
    'https://www.classcentral.com/signup',
    'https://www.classcentral.com/report/best-free-online-courses-2022/'
        ]
web_crawler = WebCrawler(web_url1).translate_all_page("output78.html")
#linkss = web_crawler.get_all_links()
#for i, n in enumerate(list(set(linkss))):
#    print(i, n)
#x = 78
#linkss_new = list(set(linkss))

#print(len(set(downloaded_links)))
#for num, link in enumerate(linkss_new):
    #if link.strip() == 'https://www.classcentral.com/institution/amazon' or link.strip() == 'https://www.classcentral.com/institution/smithsonian' or link.strip() == 'https://www.classcentral.com/report/author/manoel/' or link.strip() == 'https://www.classcentral.com/university/mit' or link.strip() == 'https://www.classcentral.com/provider/swayam' or link.strip() == 'https://www.classcentral.com/report/' or link.strip() == 'https://www.classcentral.com/provider/futurelearn' or link.strip() == 'https://www.classcentral.com/report/most-popular-online-courses/' or link.strip() == 'https://www.classcentral.com/provider/udemy' or link.strip() == 'https://www.classcentral.com/rankings' or link.strip() == 'https://www.classcentral.com/university/stanford' or link.strip() == 'https://www.classcentral.com/report/online-learning-deals/' or link.strip() == 'https://www.classcentral.com/help/moocs' or link.strip() == 'https://www.classcentral.com/subject/personal-development' or link.strip() == 'https://www.classcentral.com/course/mindfulness-wellbeing-performance-3714':
    #    linkss_new.remove(link)
    #if link.strip() not in downloaded_links:
    #    print(num, link)

        #WebCrawler(link.strip()).translate_all_page("output{}.html".format(x))
        #x += 1

