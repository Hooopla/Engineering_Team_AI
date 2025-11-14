class Account:
    """
    A class to manage a user's trading account, including balance management and transaction tracking.
    """

    def __init__(self, username: str, initial_deposit: float):
        """
        Initializes the account with a username and an initial deposit.
        
        :param username: The name of the user.
        :param initial_deposit: The initial amount of money to deposit into the account.
        """
        self.username = username
        self.balance = initial_deposit
        self.holdings = {}  # Dictionary to hold stock symbols and quantities
        self.transactions = []  # List to hold all transactions
    
    def deposit(self, amount: float) -> None:
        """
        Deposits an amount into the account.

        :param amount: The amount of money to deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraws an amount from the account.
        
        :param amount: The amount of money to withdraw.
        :raises ValueError: If the withdrawal would leave the balance negative.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: ${amount:.2f}")

    def buy_shares(self, symbol: str, quantity: int) -> None:
        """
        Buys shares of a stock given a symbol and quantity.

        :param symbol: The stock symbol to buy shares of.
        :param quantity: The number of shares to purchase.
        :raises ValueError: If there are insufficient funds or an invalid quantity is specified.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        share_price = get_share_price(symbol)
        total_cost = share_price * quantity
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to buy shares.")
        self.balance -= total_cost
        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        self.transactions.append(f"Bought {quantity} shares of {symbol} at ${share_price:.2f} each.")

    def sell_shares(self, symbol: str, quantity: int) -> None:
        """
        Sells shares of a stock given a symbol and quantity.

        :param symbol: The stock symbol to sell shares of.
        :param quantity: The number of shares to sell.
        :raises ValueError: If the user attempts to sell more shares than owned.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError("Insufficient shares to sell.")
        share_price = get_share_price(symbol)
        total_revenue = share_price * quantity
        self.balance += total_revenue
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transactions.append(f"Sold {quantity} shares of {symbol} at ${share_price:.2f} each.")

    def calculate_portfolio_value(self) -> float:
        """
        Calculates the total value of the user's stock portfolio.

        :return: The total value of the portfolio.
        """
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def calculate_profit_loss(self) -> float:
        """
        Calculates the profit or loss from the initial deposit.

        :return: The profit or loss amount.
        """
        initial_investment = self.balance + sum(get_share_price(symbol) * quantity for symbol, quantity in self.holdings.items())
        return self.calculate_portfolio_value() - initial_investment

    def get_holdings(self) -> dict:
        """
        Reports the current holdings of the user.

        :return: A dictionary of stock symbols and their respective quantities.
        """
        return self.holdings

    def get_profit_loss(self) -> float:
        """
        Reports the current profit or loss of the user.

        :return: The profit or loss amount.
        """
        return self.calculate_profit_loss()

    def list_transactions(self) -> list:
        """
        Lists all transactions made by the user.

        :return: A list of transaction strings.
        """
        return self.transactions


def get_share_price(symbol: str) -> float:
    """
    Returns the current price of a share based on the provided symbol.

    :param symbol: The stock symbol.
    :return: The current price of the share.
    """
    share_prices = {
        'AAPL': 150.0,
        'TSLA': 700.0,
        'GOOGL': 2800.0
    }
    return share_prices.get(symbol, 0.0)