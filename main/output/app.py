import gradio as gr
from accounts import Account, get_share_price

# Create a single user account for simplicity
user_account = Account(user_id="user1", initial_deposit=10000.0)

def create_account(initial_deposit):
    global user_account
    user_account = Account(user_id="user1", initial_deposit=initial_deposit)
    return f"Account created with initial deposit: ${initial_deposit}"

def deposit(amount):
    user_account.deposit(amount)
    return f"Deposited ${amount}. Current balance: ${user_account.balance}"

def withdraw(amount):
    if user_account.withdraw(amount):
        return f"Withdrew ${amount}. Current balance: ${user_account.balance}"
    else:
        return "Insufficient balance to withdraw the requested amount."

def buy_shares(symbol, quantity):
    if user_account.buy_shares(symbol, quantity):
        return f"Bought {quantity} shares of {symbol}. Balance: ${user_account.balance}"
    else:
        return "Insufficient funds to buy the requested shares."

def sell_shares(symbol, quantity):
    if user_account.sell_shares(symbol, quantity):
        return f"Sold {quantity} shares of {symbol}. Balance: ${user_account.balance}"
    else:
        return "Insufficient shares to sell."

def get_portfolio():
    holdings = user_account.get_holdings()
    portfolio_value = user_account.get_portfolio_value()
    return f"Holdings: {holdings}. Portfolio value: ${portfolio_value}"

def get_profit_loss():
    profit_or_loss = user_account.get_profit_or_loss()
    return f"Profit/Loss since initial deposit: ${profit_or_loss}"

def get_transaction_history():
    transactions = user_account.get_transaction_history()
    return f"Transactions: {transactions}"

# Gradio UI components
with gr.Blocks() as demo:
    gr.Markdown("# Trading Simulation Platform")
    
    with gr.Tab("Account"):
        initial_deposit_input = gr.Number(label="Initial Deposit")
        account_creation_btn = gr.Button("Create Account")
        account_output = gr.Text(interactive=False)
        account_creation_btn.click(create_account, [initial_deposit_input], account_output)

    with gr.Tab("Deposit & Withdraw"):
        deposit_input = gr.Number(label="Amount to Deposit")
        deposit_btn = gr.Button("Deposit")
        deposit_output = gr.Text(interactive=False)
        deposit_btn.click(deposit, [deposit_input], deposit_output)

        withdraw_input = gr.Number(label="Amount to Withdraw")
        withdraw_btn = gr.Button("Withdraw")
        withdraw_output = gr.Text(interactive=False)
        withdraw_btn.click(withdraw, [withdraw_input], withdraw_output)

    with gr.Tab("Buy & Sell Shares"):
        buy_symbol_input = gr.Text(label="Symbol to Buy")
        buy_quantity_input = gr.Number(label="Quantity to Buy")
        buy_btn = gr.Button("Buy Shares")
        buy_output = gr.Text(interactive=False)
        buy_btn.click(buy_shares, [buy_symbol_input, buy_quantity_input], buy_output)

        sell_symbol_input = gr.Text(label="Symbol to Sell")
        sell_quantity_input = gr.Number(label="Quantity to Sell")
        sell_btn = gr.Button("Sell Shares")
        sell_output = gr.Text(interactive=False)
        sell_btn.click(sell_shares, [sell_symbol_input, sell_quantity_input], sell_output)

    with gr.Tab("Reports"):
        holdings_btn = gr.Button("Get Portfolio")
        holdings_output = gr.Text(interactive=False)
        holdings_btn.click(get_portfolio, [], holdings_output)

        profit_loss_btn = gr.Button("Get Profit/Loss")
        profit_loss_output = gr.Text(interactive=False)
        profit_loss_btn.click(get_profit_loss, [], profit_loss_output)

        transaction_history_btn = gr.Button("Get Transactions")
        transaction_history_output = gr.Text(interactive=False)
        transaction_history_btn.click(get_transaction_history, [], transaction_history_output)

demo.launch()