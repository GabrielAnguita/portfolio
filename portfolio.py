from __future__ import annotations

from typing import TypeAlias
from dataclasses import dataclass
from datetime import date
import random

Ticker: TypeAlias = str

@dataclass
class Stock:
    ticker: Ticker

    def get_price(self, date: date) -> float:
        """
        Mock method for obtaining the price of a stock on a given date.
        We seed the random module with both the date and the stock's ticker for
        the sake of getting consistent results across a single test run.

        Here, we would query a database or an external API for getting actual results,
        but it goes beyond the scope of the requirements.

        We will assume all stock prices are represented in the same currency and won't bother thinking about
        that in this module.
        """
        random.seed(hash(date) + hash(self.ticker))
        return random.random()


@dataclass
class StockHolding:
    stock: Stock
    amount: int # could have been float or decimal, if we'd considered fractional shares

    def get_value_on_date(self, date: date) -> float:
        """Date in, stock value at said date out"""
        return self.stock.get_price(date) * self.amount


@dataclass
class Portfolio:
    stocks: dict[Ticker, StockHolding]

    def get_portfolio_value_on_date(self, date: date) -> float:
        """
        Return the value of the whole portfolio on a given date.
        """
        return sum(
            stock_holding.get_value_on_date(date)
            for stock_holding in self.stocks.values()
        )

    def get_profit(
        self,
        start_date: date,
        end_date: date,
        annualized: bool = False,
     ) -> float:
        """
        Return the profit of the whole portfolio between a start and an end date,
        as a rate of return.

        If <annualized> is True, return the annualized profit.
        """
        if start_date >= end_date:
            raise Exception("<end_date> must be grater than <start_date>")
        profit = (self.get_portfolio_value_on_date(end_date) / self.get_portfolio_value_on_date(start_date)) - 1
        if annualized:
            return self.annualize_profit(start_date, end_date, profit)
        return round(profit, 4)

    def annualize_profit(
        self,
        start_date: date,
        end_date: date,
        profit: float,
    ) -> float:
        """
        Reference:
        https://www.investopedia.com/terms/a/annual-return.asp
        """
        days = (end_date - start_date).days
        years = days / 365
        compound_annual_growth_rate = (1 + profit) ** (1 / years) - 1
        return round(compound_annual_growth_rate, 4)
        
    @classmethod
    def from_dict(
            cls,
            data: dict[Ticker, int] | None = None,
            **kwargs
        ) -> 'Portfolio':
        """
        Return an instance of Portfolio (or any subclass), built from a dict whose
        keys are Stock tickers and its values are ints representing the amount held.
        Can also take kwargs with the same logic.
        """
        if data is None:
            data = kwargs
        else:
            data.update(kwargs)

        return cls(
            {
                ticker: (
                    StockHolding(
                        stock=Stock(ticker=ticker),
                        amount=amount,
                    )
                )
                for ticker, amount in data.items()
            }
        )
