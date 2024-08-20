from portfolio import Portfolio
from datetime import date

def run_examples() -> None:
    portfolio = Portfolio.from_dict(
        GOOG=5,
        POOG=1,
        CHUG=10,
    )
    for start_date, end_date in (
        (date(2020, 12, 1), date(2021, 12, 1)),
        (date(2020, 12, 1), date(2022, 12, 1)),
    ):
        profit = portfolio.get_profit(start_date, end_date)
        start_value = portfolio.get_portfolio_value_on_date(start_date)
        end_value = portfolio.get_portfolio_value_on_date(end_date)
        annualized_profit = portfolio.get_profit(start_date, end_date, annualized=True)
        print(
            "\nThe portfolio's value at {} is {}.".format(
                start_date, start_value,
            )
        )
        print(
            "The portfolio's value at {} is {}.".format(
                end_date, end_value,
            )
        )
        print(
            "The portfolio's profit between {} and {} is {}.".format(
                start_date, end_date, profit
            )
        )
        print(
            "The portfolio's annualized profit between {} and {} is {}.".format(
                start_date, end_date, annualized_profit
            )
        )


if __name__ == "__main__":
    run_examples()    
