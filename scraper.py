#!/usr/bin/env python3.7

from urllib.request import urlopen
from bs4 import BeautifulSoup # sudo apt-get install python3-bs4
from re import compile
from paper import Paper

FUNDAMENTUS_URL = 'https://www.fundamentus.com.br/'
FUNDAMENTUS_DETAILS = 'detalhes.php'
FUNDAMENTUS_DETAILS_URL = FUNDAMENTUS_URL + FUNDAMENTUS_DETAILS
FUNDAMENTUS_DETAILS_PAPER_URL = FUNDAMENTUS_DETAILS_URL + '?papel='

EBIT_12_INDEX = 106
ENTERPRISE_VALUE_INDEX = 21

def fetch_papers():
    return [Paper('ITSA4',201000000,120243000000,0.03,245725000), Paper('ABEV3',16314100000,286896000000,0.214,345031000) ]
    #page = urlopen(FUNDAMENTUS_DETAILS_URL)

    #soup = BeautifulSoup(page, 'html.parser')

    #papers_sumary = soup.find_all(__has_not_class_attr, href=compile(FUNDAMENTUS_DETAILS))

    #papers = []
    #for paper_sumary in papers_sumary:
    #    paperHref = paper_sumary[0].attrs['href']
    #    papers.append(detailer(FUNDAMENTUS_URL + paperHref))

    #return papers

def __detailer(url):
    pass
    #page = urlopen(url)

    #soup = BeautifulSoup(page, 'html.parser')

    #EBIT = soup.find_all('span', attrs={'class': 'txt'})[EBIT_12_INDEX].text.replace('.', '')

    #enterprise_value = soup.find_all('span', attrs={'class': 'txt'})[ENTERPRISE_VALUE_INDEX].text.replace('.', '')

    #return Paper()

def __has_not_class_attr(tag):
    return not tag.has_attr('class')