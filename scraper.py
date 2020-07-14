#!/usr/bin/env python3.7

import sys
import writer
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup # sudo apt-get install python3-bs4
from re import compile
from paper import Paper
from time import sleep


FUNDAMENTUS_URL ='https://www.fundamentus.com.br/resultado.php'
header = {'User-Agent': 'Mozilla/5.0'}

WAITING_TIME = 1 # Strongly recommend not to decrease this value, we do not want to harm those who help us

CODE_INDEX = 1
EV_PER_EBIT_INDEX = 21
LIQUIDITY_INDEX = 35
ROIC_INDEX = 31
ROE_INDEX = 33

def fetch_papers():
    
    req = Request(FUNDAMENTUS_URL, headers=header)
    page = urlopen(req)

    soup = BeautifulSoup(page, 'html.parser')
    paper_rows = soup.find_all(["tr"])

    __discartTableHeader(paper_rows)

    papers = []

    for idx, paper_row in enumerate(paper_rows, start=1):
        papers.append(__detailer(paper_row.contents))
        print("Progress: " + str(idx) + "/" + str(len(paper_rows)) + "\n")

    return papers

def __detailer(paper_detail):

    code = paper_detail[CODE_INDEX].text.replace('.', '')
    print("Detailing " + code)

    try:
        ev_per_ebit = float(paper_detail[EV_PER_EBIT_INDEX].text.replace('.', '').replace(',', '.'))

        roic_text = paper_detail[ROIC_INDEX].text.replace('\n', '').replace('.', '').replace(' ', '').replace(',', '.').replace('%', '')
        roic = float(roic_text)/100 if(roic_text != '-') else 0

        roe_text = paper_detail[ROE_INDEX].text.replace('\n', '').replace('.', '').replace(' ', '').replace(',', '.').replace('%', '')
        roe = float(roe_text)/100 if(roe_text != '-') else 0

        liquidity = int(paper_detail[LIQUIDITY_INDEX].text.replace('.', '').replace(',', ''))/100

        return Paper(code, ev_per_ebit, roic, roe, liquidity)

    except:
        print("Couldn't detail " + code)
        writer.log_error(code, str(sys.exc_info()[0]))

        return Paper(code, 0, 0, 0, 0)

def __discartTableHeader(paper_rows):
    paper_rows.pop(0)

def __has_not_class_attr(tag):
    return not tag.has_attr('class')