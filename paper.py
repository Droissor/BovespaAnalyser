#!/usr/bin/env python3.7

class Paper:
    def __init__(self, code, enterprise_value_per_earning, return_on_invested_capital, return_on_equity, liquidity):
        self.code = code
        self.enterprise_value_per_earning = enterprise_value_per_earning
        self.return_on_invested_capital = return_on_invested_capital
        self.return_on_equity = return_on_equity
        self.liquidity = liquidity

    def get_enterprise_value_per_earning(self):
        return self.enterprise_value_per_earning

    def get_magic_number(self):
        return round(self.enterprise_value_per_earning / self.return_on_invested_capital, 4)