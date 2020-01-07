#!/usr/bin/env python3.7

class Paper:
    def __init__(self, code, earnings_before_interest_and_taxes, enterprise_value, return_on_invested_capital, liquidity):
        self.code = code
        self.earnings_before_interest_and_taxes = earnings_before_interest_and_taxes
        self.liquidity = liquidity
        self.enterprise_value = enterprise_value
        self.return_on_invested_capital = return_on_invested_capital

    def get_earnings_yield(self):
        return self.earnings_before_interest_and_taxes / self.enterprise_value if(self.enterprise_value > 0) else 0

    def get_enterprise_value_per_earning(self):
        return self.enterprise_value / self.earnings_before_interest_and_taxes if(self.earnings_before_interest_and_taxes > 0) else 0