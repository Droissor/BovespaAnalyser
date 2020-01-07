#!/usr/bin/env python3.7

import os
import csv
from paper import Paper

def export_to_csv(filename, papers_rank):

    local_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(local_dir, filename + '.csv'), 'w') as csv_file:    
        writer = csv.writer(csv_file)
        writer.writerow(['RANK','PAPER CODE','EARNINGS BEFORE INTEREST AND TAXES (EBIT)', 'ENTERPRISE VALUE (EV)','EV/EBIT','EBIT/EV','RETURN ON INVESTED CAPITAL (ROIC)','LIQUIDITY LAST 2 MONTHS'])
        
        for idx, paper in enumerate(papers_rank, start=1):
            writer.writerow([idx, paper.code, paper.earnings_before_interest_and_taxes, paper.enterprise_value, paper.get_enterprise_value_per_earning(),
                            paper.get_earnings_yield(), paper.return_on_invested_capital,  paper.liquidity])