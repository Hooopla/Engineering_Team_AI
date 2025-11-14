import gradio as gr
from accounts import Account

def create_account(username, initial_deposit):
    global user_account
    user_account = Account(username, float(initial_deposit))
    return f"Account created for {username} with an initial deposit of ${initial_deposit:.2f}"

def deposit_funds(amount):
    user_account.deposit(float(amount))
    return f"Deposited: ${amount:.2f}. Current balance: ${user_account.balance:.2f}"

def withdraw_funds(amount):
    user_account.withdraw(float(amount))
    return f"Withdrew: ${amount:.2f}. Current balance: ${user_account.balance:.2f}"

def buy_shares(symbol, quantity):
    user_account.buy_shares(symbol, int(quantity))
    return f"Bought {quantity} shares of {symbol}. Current holdings: {user_account.get_holdings()}"

def sell_shares(symbol, quantity):
    user_account.sell_shares(symbol, int(quantity))
    return f"Sold {quantity} shares of {symbol}. Current holdings: {user_account.get_holdings()}"

def portfolio_value():
    return f"Total portfolio value: ${user_account.calculate_portfolio_value():.2f}"

def profit_loss():
    return f"Profit/Loss: ${user_account.get_profit_loss():.2f}"

def list_transactions():
    return "\n".join(user_account.list_transactions())

user_account = None

with gr.Blocks() as demo:
    gr.Markdown("# Trading Account Management")
    
    with gr.Tab("Create Account"):
        username = gr.Textbox(label="Username")
        initial_deposit = gr.Number(label="Initial Deposit", value=1000)
        create_btn = gr.Button("Create Account")
        create_output = gr.Textbox(label="Output", interactive=False)
        create_btn.click(create_account, inputs=[username, initial_deposit], outputs=create_output)

    with gr.Tab("Manage Funds"):
        deposit_amount = gr.Number(label="Deposit Amount", value=100)
        deposit_btn = gr.Button("Deposit")
        deposit_output = gr.Textbox(label="Output", interactive=False)
        deposit_btn.click(deposit_funds, inputs=deposit_amount, outputs=deposit_output)
        
        withdraw_amount = gr.Number(label="Withdraw Amount", value=100)
        withdraw_btn = gr.Button("Withdraw")
        withdraw_output = gr.Textbox(label="Output", interactive=False)
        withdraw_btn.click(withdraw_funds, inputs=withdraw_amount, outputs=withdraw_output)
    
    with gr.Tab("Buy/Sell Shares"):
        share_symbol = gr.Textbox(label="Stock Symbol", placeholder="AAPL, TSLA, GOOGL")
        share_quantity = gr.Number(label="Quantity", value=1)
        
        buy_btn = gr.Button("Buy Shares")
        buy_output = gr.Textbox(label="Output", interactive=False)
        buy_btn.click(buy_shares, inputs=[share_symbol, share_quantity], outputs=buy_output)
        
        sell_btn = gr.Button("Sell Shares")
        sell_output = gr.Textbox(label="Output", interactive=False)
        sell_btn.click(sell_shares, inputs=[share_symbol, share_quantity], outputs=sell_output)

    with gr.Tab("Portfolio"):
        value_btn = gr.Button("Portfolio Value")
        value_output = gr.Textbox(label="Output", interactive=False)
        value_btn.click(portfolio_value, outputs=value_output)
        
        profit_loss_btn = gr.Button("Profit/Loss")
        profit_loss_output = gr.Textbox(label="Output", interactive=False)
        profit_loss_btn.click(profit_loss, outputs=profit_loss_output)

    with gr.Tab("Transactions"):
        transactions_btn = gr.Button("List Transactions")
        transactions_output = gr.Textbox(label="Output", interactive=False)
        transactions_btn.click(list_transactions, outputs=transactions_output)

demo.launch()