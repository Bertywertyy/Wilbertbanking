import streamlit as st

# BankAccount class to manage balance
class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}"
        elif amount > self.balance:
            return "Insufficient funds."
        return "Withdrawal amount must be positive."

    def get_balance(self):
        return f"Current balance: ${self.balance:.2f}"

# Create a global bank account
account = BankAccount()

# Streamlit UI
st.title("Banking System")

# Display current balance
st.write(account.get_balance())

# Deposit form
st.subheader("Deposit")
deposit_amount = st.number_input("Enter amount to deposit", min_value=0.0, step=0.01)
if st.button("Deposit"):
    deposit_message = account.deposit(deposit_amount)
    st.success(deposit_message)

# Withdraw form
st.subheader("Withdraw")
withdraw_amount = st.number_input("Enter amount to withdraw", min_value=0.0, step=0.01)
if st.button("Withdraw"):
    withdraw_message = account.withdraw(withdraw_amount)
    st.success(withdraw_message)

# Show updated balance after any transaction
st.write(account.get_balance())
