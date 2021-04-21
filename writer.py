#!/usr/bin/env python3.7

import os
import csv
from paper import Paper
from time import sleep
from datetime import datetime

def export_to_csv(filename, paper_rank_list):

    local_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(local_dir, filename + '.csv'), 'w') as csv_file:    
        writer = csv.writer(csv_file)
        writer.writerow(['RANK','RANK POINTS (0 is better)','PAPER CODE', 'EV/EBIT', 'RETURN ON EQUITY (ROE)','RETURN ON INVESTED CAPITAL (ROIC)','LIQUIDITY LAST 2 MONTHS', 'SETOR', 'SUBSETOR'])
        
        for idx, paper_rank in enumerate(paper_rank_list, start=1):
            writer.writerow([idx, paper_rank[1], paper_rank[0].code, paper_rank[0].enterprise_value_per_earning,
                            paper_rank[0].return_on_equity, paper_rank[0].return_on_invested_capital, paper_rank[0].liquidity,
                            paper_rank[0].setor, paper_rank[0].subSetor])

def log_error(url, err):

    local_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(local_dir, 'log_err.txt'), 'a') as log_error_file: 
        log_error_file.write("\n" + str(datetime.now()) + ":   Couldn't detail " + url + "\nException is: " + err + "\n")