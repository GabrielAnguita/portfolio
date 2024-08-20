# Portfolio Profit Calculator

This project implements a simple Portfolio class that calculates the profit of a collection of stocks between two dates. It also includes a bonus feature to calculate the annualized return.

## Requirements

- Python 3.11 or higher
- Poetry (for dependency management)

## Setup

1. Clone the repository:
   ```
   git clone git@github.com:GabrielAnguita/portfolio.git
   cd portfolio-profit
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

## Project Structure

- `portfolio.py`: Contains the main implementation of the Portfolio class and related classes.
- `pyproject.toml`: Poetry configuration file with project metadata and dependencies.
- `tests.py`: A few tests.
- `examples.py`: Examples.

## Usage

To run the example calculations:

```
poetry run python examples.py
```

This will execute the `run_examples()` function in `examples.py`, which demonstrates the usage of the Portfolio class with sample data.

## Testing

To run tests:

```
poetry run pytest tests.py
```

## Implementation Details

- The `Stock` class has a `get_price` method that returns a mock price for demonstration purposes.
- The `Portfolio` class calculates both simple and annualized profits between two dates.
- The `annualize_profit` method uses the Compound Annual Growth Rate (CAGR) formula.

## Bonus Feature

The `get_profit` method includes an optional `annualized` parameter. When set to `True`, it returns the annualized return of the portfolio between the given dates.

## Notes for Reviewers

- The current implementation uses mock data for stock prices. In a real-world scenario, this would be replaced with actual market data.
- The project structure is set up using Poetry for dependency management, making it easy to install and run.
- Feel free to modify the example in `run_examples()` or create your own Portfolio instances to test different scenarios.

If you have any questions or need further clarification, please don't hesitate to ask!
