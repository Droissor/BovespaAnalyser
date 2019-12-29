#!/usr/bin/env python3.7

from urllib.request import urlopen
from bs4 import BeautifulSoup # sudo apt-get install python3-bs4
from re import compile

FUNDAMENTUS_URL = 'https://www.fundamentus.com.br/'
FUNDAMENTUS_DETAILS = 'detalhes.php'
FUNDAMENTUS_DETAILS_URL = FUNDAMENTUS_URL + FUNDAMENTUS_DETAILS
FUNDAMENTUS_DETAILS_PAPER_URL = FUNDAMENTUS_DETAILS_URL + '?papel='

EBIT_12_INDEX = 106
ENTERPRISE_VALUE_INDEX = 21

def main():  
    papers = fetch_papers()

    rank_papers(papers)

def fetch_papers():
    page = urlopen(FUNDAMENTUS_DETAILS_URL)

    soup = BeautifulSoup(page, 'html.parser')

    return soup.find_all(has_not_class_attr, href=compile(FUNDAMENTUS_DETAILS))

def rank_papers(papers):

#    values = []
#    for paper in papers:
#        paperRef = papers[0].attrs['href']
#        values.append(detailer( paperHref))

    paperHref = papers[3].attrs['href']

    print(detailer(paperHref))


def detailer(href):
    page = urlopen(FUNDAMENTUS_URL + href)

    soup = BeautifulSoup(page, 'html.parser')

    ebit = soup.find_all('span', attrs={'class': 'txt'})[EBIT_12_INDEX].text.replace('.', '')

    enterprise_value = soup.find_all('span', attrs={'class': 'txt'})[ENTERPRISE_VALUE_INDEX].text.replace('.', '')

    return calculate_value(float(ebit), float(enterprise_value))

def calculate_value(ebit, enterprise_value):
    
    value = 0

    if(ebit > 0):
        value = enterprise_value / ebit

    return value

def has_not_class_attr(tag):
    return not tag.has_attr('class')

if __name__ == "__main__":
	main()