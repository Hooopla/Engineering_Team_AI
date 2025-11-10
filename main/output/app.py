import gradio as gr
from accounts import Account

def create_account(username, initial_deposit):
    global account
    account = Account(username, float(initial_deposit))
    return f"Account created for {username} with an initial deposit of {initial_deposit}."

def deposit_funds(amount):
    account.deposit(float(amount))
    return f"Deposited {amount}. Current balance: {account.balance}"

def withdraw_funds(amount):
    try:
        account.withdraw(float(amount))
        return f"Withdrew {amount}. Current balance: {account.balance}"
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        account.buy_shares(symbol, int(quantity))
        return f"Bought {quantity} shares of {symbol}. Current holdings: {account.get_holdings()}"
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        account.sell_shares(symbol, int(quantity))
        return f"Sold {quantity} shares of {symbol}. Current holdings: {account.get_holdings()}"
    except ValueError as e:
        return str(e)

def portfolio_value():
    return f"Total Portfolio Value: {account.get_portfolio_value()}"

def profit_or_loss():
    return f"Profit/Loss: {account.get_profit_or_loss()}"

def holdings():
    return f"Current Holdings: {account.get_holdings()}"

def transactions():
    return f"Transaction History: {account.list_transactions()}"

with gr.Interface() as demo:
    gr.Markdown("### Simple Trading Account Management")
    username = gr.Textbox(label="Username")
    initial_deposit = gr.Textbox(label="Initial Deposit", type="number")
    create_button = gr.Button("Create Account")
    create_button.click(create_account, inputs=[username, initial_deposit], outputs="text")
    
    deposit_amount = gr.Textbox(label="Deposit Amount", type="number")
    deposit_button = gr.Button("Deposit")
    deposit_button.click(deposit_funds, inputs=deposit_amount, outputs="text")
    
    withdraw_amount = gr.Textbox(label="Withdraw Amount", type="number")
    withdraw_button = gr.Button("Withdraw")
    withdraw_button.click(withdraw_funds, inputs=withdraw_amount, outputs="text")
    
    buy_symbol = gr.Textbox(label="Buy Symbol")
    buy_quantity = gr.Textbox(label="Buy Quantity", type="number")
    buy_button = gr.Button("Buy")
    buy_button.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs="text")
    
    sell_symbol = gr.Textbox(label="Sell Symbol")
    sell_quantity = gr.Textbox(label="Sell Quantity", type="number")
    sell_button = gr.Button("Sell")
    sell_button.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs="text")
    
    portfolio_button = gr.Button("Get Portfolio Value")
    portfolio_button.click(portfolio_value, outputs="text")
    
    profit_button = gr.Button("Get Profit/Loss")
    profit_button.click(profit_or_loss, outputs="text")
    
    holdings_button = gr.Button("Get Holdings")
    holdings_button.click(holdings, outputs="text")
    
    transactions_button = gr.Button("Get Transactions")
    transactions_button.click(transactions, outputs="text")

demo.launch()