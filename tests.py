import pytest
from datetime import date
import math

from .portfolio import Portfolio

@pytest.fixture
def sample_portfolio():
    return Portfolio.from_dict(
        AAPL=10,
        GOOGL=5,
        MSFT=8
    )

def test_annualize_profit_one_year():
    portfolio = Portfolio.from_dict(AAPL=1)
    start_date = date(2020, 1, 1)
    end_date = date(2021, 1, 1)
    profit = 0.1

    annualized_profit = portfolio.annualize_profit(start_date, end_date, profit)
    assert math.isclose(annualized_profit, profit, abs_tol=0.001)

def test_annualize_profit_two_years():
    portfolio = Portfolio.from_dict(AAPL=1)
    start_date = date(2020, 1, 1)
    end_date = date(2022, 1, 1)
    profit = 0.21

    annualized_profit = portfolio.annualize_profit(start_date, end_date, profit)
    expected = (1 + 0.21) ** (1/2) - 1  # (1 + total_return)^(1/years) - 1
    assert math.isclose(annualized_profit, expected, abs_tol=0.001)

def test_annualize_profit_partial_year():
    portfolio = Portfolio.from_dict(AAPL=1)
    start_date = date(2020, 1, 1)
    end_date = date(2020, 7, 1)  # 182 days
    profit = 0.05  # 5% profit over 182 days

    annualized_profit = portfolio.annualize_profit(start_date, end_date, profit)
    expected = (1 + 0.05) ** (365/182) - 1
    assert math.isclose(annualized_profit, expected, abs_tol=0.001)
