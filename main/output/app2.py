import gradio as gr
from accounts import Account

account = None
username = gr.Textbox(label="Username")
initial_deposit = gr.Number(label="Initial Deposit")
output_text = gr.Textbox()

def create_account(username, initial_deposit):
    global account
    account = Account(username, float(initial_deposit))
    return f"Account created for {username} with initial deposit of ${initial_deposit:.2f}"

def deposit_funds(amount):
    global account
    account.deposit(float(amount))
    return f"Deposited ${amount:.2f}. Current balance: ${account.balance:.2f}"

def withdraw_funds(amount):
    global account
    try:
        account.withdraw(float(amount))
        return f"Withdrew ${amount:.2f}. Current balance: ${account.balance:.2f}"
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    global account
    try:
        account.buy_shares(symbol, int(quantity))
        return f"Bought {quantity} shares of {symbol}. Current holdings: {account.holdings}"
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    global account
    try:
        account.sell_shares(symbol, int(quantity))
        return f"Sold {quantity} shares of {symbol}. Current holdings: {account.holdings}"
    except ValueError as e:
        return str(e)

def portfolio_value():
    global account
    return f"Total portfolio value: ${account.portfolio_value():.2f}"

def profit_loss():
    global account
    return f"Profit/Loss: ${account.profit_loss():.2f}"

def report_holdings():
    global account
    return f"Current holdings: {account.report_holdings()}"

def report_transactions():
    global account
    return f"Transaction history: {account.report_transaction_history()}"

with gr.Blocks() as demo:
    gr.Markdown("### Trading Account Management System")
    username = gr.Textbox(label="Username")
    initial_deposit = gr.Number(label="Initial Deposit", value=0.0)
    create_btn = gr.Button("Create Account")
    create_btn.click(create_account, inputs=[username, initial_deposit], outputs=output_text)
    
    amount = gr.Number(label="Amount")
    withdraw_btn = gr.Button("Withdraw Funds")
    withdraw_btn.click(withdraw_funds, inputs=amount, outputs=output_text)
    
    deposit_btn = gr.Button("Deposit Funds")
    deposit_btn.click(deposit_funds, inputs=amount, outputs=output_text)
    
    symbol = gr.Textbox(label="Stock Symbol")
    quantity = gr.Number(label="Quantity")
    buy_btn = gr.Button("Buy Shares")
    buy_btn.click(buy_shares, inputs=[symbol, quantity], outputs=output_text)
    
    sell_btn = gr.Button("Sell Shares")
    sell_btn.click(sell_shares, inputs=[symbol, quantity], outputs=output_text)

    portfolio_btn = gr.Button("Portfolio Value")
    portfolio_btn.click(portfolio_value, outputs=output_text)

    profit_loss_btn = gr.Button("Profit/Loss")
    profit_loss_btn.click(profit_loss, outputs=output_text)

    holdings_btn = gr.Button("Report Holdings")
    holdings_btn.click(report_holdings, outputs=output_text)

    transactions_btn = gr.Button("Report Transactions")
    transactions_btn.click(report_transactions, outputs=output_text)

demo.launch()