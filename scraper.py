#!/usr/bin/env python3.7

import sys
import writer
from urllib.request import urlopen
from bs4 import BeautifulSoup # sudo apt-get install python3-bs4
from re import compile
from paper import Paper
from time import sleep

FUNDAMENTUS_URL = 'https://www.fundamentus.com.br/'
FUNDAMENTUS_DETAILS = 'detalhes.php'
FUNDAMENTUS_DETAILS_URL = FUNDAMENTUS_URL + FUNDAMENTUS_DETAILS
FUNDAMENTUS_DETAILS_PAPER_URL = FUNDAMENTUS_DETAILS_URL + '?papel='

WAITING_TIME = 1 # Strongly recommend not to decrease this value, we do not want to harm those who help us

CODE_INDEX = 1
EBIT_INDEX = 106
LIQUIDITY_INDEX = 19
ENTERPRISE_VALUE_INDEX = 21
ROIC_INDEX = 64

def fetch_papers():
    page = urlopen(FUNDAMENTUS_DETAILS_URL)

    soup = BeautifulSoup(page, 'html.parser')

    papers_sumary = soup.find_all(__has_not_class_attr, href=compile(FUNDAMENTUS_DETAILS))
    papers = []

    for idx, paper_sumary in enumerate(papers_sumary, start=1):
        paperHref = paper_sumary.attrs['href']
        papers.append(__detailer(FUNDAMENTUS_URL + paperHref))
        print("Progress: " + str(idx) + "/" + str(len(papers_sumary)) + "\n")
        sleep(WAITING_TIME)

    return papers

def __detailer(url):

    print("Detailing " + url)

    try:
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        paper_details = soup.find_all('span', attrs={'class': 'txt'})

        code = paper_details[CODE_INDEX].text.replace('.', '')

        ebit = int(paper_details[EBIT_INDEX].text.replace('.', ''))

        enterprise_value = int(paper_details[ENTERPRISE_VALUE_INDEX].text.replace('.', ''))

        roic_text = paper_details[ROIC_INDEX].text.replace('\n', '').replace(' ', '').replace(',', '.').replace('%', '')
        roic = float(roic_text)/100 if(roic_text != '-') else 0

        liquidity = int(paper_details[LIQUIDITY_INDEX].text.replace('.', ''))

        return Paper(code, ebit, enterprise_value, roic, liquidity)

    except:
        print("Couldn't detail " + url)
        writer.log_error(url, str(sys.exc_info()[0]))

        return Paper(url, 0, 0, 0, 0)

def __has_not_class_attr(tag):
    return not tag.has_attr('class')