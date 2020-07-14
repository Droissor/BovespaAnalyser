#!/usr/bin/env python3.7

import copy
from paper import Paper
import scraper
import writer

MINIMAL_LIQUIDITY = 100000

def main():  
    papers = scraper.fetch_papers()
    
    ranks = rank_papers(papers)

    writer.export_to_csv('the_little_book_rank', ranks[0])
    writer.export_to_csv('value_investing_rank', ranks[1])

def rank_papers(papers):

    papers = list(filter(paper_code_number_filter, papers))
    papers = list(filter(minimal_liquitidy_ebit_roe_filter, papers))

    the_little_book_rank = sorted(copy.deepcopy(papers), key=lambda paper: paper.get_magic_number())
    value_investing_rank = sorted(copy.deepcopy(papers), key=lambda paper: paper.enterprise_value_per_earning)

    return [the_little_book_rank, value_investing_rank]

def minimal_liquitidy_ebit_roe_filter(paper):
    return paper.liquidity >= MINIMAL_LIQUIDITY and paper.enterprise_value_per_earning > 0 and paper.return_on_equity >= 0.10

def paper_code_number_filter(paper):
    return '3' in paper.code

if __name__ == "__main__":
	main()