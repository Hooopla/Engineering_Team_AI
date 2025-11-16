class Account:
    def __init__(self, user_id: str, initial_deposit: float) -> None:
        self.user_id = user_id
        self.balance = initial_deposit
        self.initial_deposit = initial_deposit
        self.holdings = {}
        self.transactions = []

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.transactions.append({'action': 'deposit', 'amount': amount})

    def withdraw(self, amount: float) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append({'action': 'withdraw', 'amount': amount})
            return True
        return False

    def buy_shares(self, symbol: str, quantity: int) -> bool:
        price = get_share_price(symbol)
        total_cost = price * quantity
        if total_cost <= self.balance:
            self.balance -= total_cost
            if symbol in self.holdings:
                self.holdings[symbol] += quantity
            else:
                self.holdings[symbol] = quantity
            self.transactions.append({'action': 'buy', 'symbol': symbol, 'quantity': quantity, 'price': price})
            return True
        return False

    def sell_shares(self, symbol: str, quantity: int) -> bool:
        if symbol in self.holdings and self.holdings[symbol] >= quantity:
            price = get_share_price(symbol)
            total_income = price * quantity
            self.balance += total_income
            self.holdings[symbol] -= quantity
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.transactions.append({'action': 'sell', 'symbol': symbol, 'quantity': quantity, 'price': price})
            return True
        return False

    def get_portfolio_value(self) -> float:
        total_value = 0.0
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def get_profit_or_loss(self) -> float:
        total_value = self.get_portfolio_value()
        return (self.balance + total_value) - self.initial_deposit

    def get_holdings(self) -> dict:
        return self.holdings.copy()

    def get_transaction_history(self) -> list:
        return self.transactions.copy()

# Test implementation of get_share_price
# This would typically call an external API; here it returns fixed prices for testing.
def get_share_price(symbol: str) -> float:
    prices = {'AAPL': 150.0, 'TSLA': 750.0, 'GOOGL': 2800.0}
    return prices.get(symbol, 0.0)