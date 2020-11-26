#!/usr/bin/env python3.7

import copy
from paper import Paper
import scraper
import writer

MINIMAL_LIQUIDITY = 100000

def main():  
    papers = scraper.fetch_papers()
    
    ranks = rank_papers(papers)

    writer.export_to_csv('value_investing_rank', ranks)

def rank_papers(papers):

    papers = list(filter(paper_code_number_filter, papers))
    papers = list(filter(minimal_liquitidy_ebit_roe_filter, papers))

    roic_rank = sorted(copy.deepcopy(papers), key=lambda paper: paper.return_on_invested_capital, reverse=True)
    earnings_yield_rank = sorted(copy.deepcopy(papers), key=lambda paper: paper.enterprise_value_per_earning)

    value_investing_rank = []

    for paper in papers:

        paper_filtered = filter(lambda paper_roic: paper_roic.code == paper.code, roic_rank)
        roic_rank_index = roic_rank.index(next(paper_filtered))

        paper_filtered = filter(lambda paper_earnings_yield: paper_earnings_yield.code == paper.code, earnings_yield_rank)
        earnings_yield_rank_index = earnings_yield_rank.index(next(paper_filtered))

        value_investing_rank.append([paper, roic_rank_index+earnings_yield_rank_index])

    value_investing_rank = sorted(value_investing_rank, key=lambda paper_rank: paper_rank[1])

    return value_investing_rank

def minimal_liquitidy_ebit_roe_filter(paper):
    return paper.liquidity >= MINIMAL_LIQUIDITY and paper.enterprise_value_per_earning > 0 and paper.return_on_equity >= 0.10

def paper_code_number_filter(paper):
    return '3' in paper.code or '4' in paper.code

if __name__ == "__main__":
	main()