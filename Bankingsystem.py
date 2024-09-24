import streamlit as st

# Initialize session state for balance if it doesn't exist
if 'balance' not in st.session_state:
    st.session_state.balance = 0.0

# BankAccount class to manage balance (using session state)
class BankAccount:
    def deposit(self, amount):
        if amount > 0:
            st.session_state.balance += amount
            return f"Deposited: ${amount:.2f}. New balance: ${st.session_state.balance:.2f}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= st.session_state.balance:
            st.session_state.balance -= amount
            return f"Withdrew: ${amount:.2f}. New balance: ${st.session_state.balance:.2f}"
        elif amount > st.session_state.balance:
            return "Insufficient funds."
        return "Withdrawal amount must be positive."

    def get_balance(self):
        return f"Current balance: ${st.session_state.balance:.2f}"

# Create a bank account instance
account = BankAccount()

# Streamlit UI
st.title("Banking System")

# Display current balance
st.header(f"Current balance: ${st.session_state.balance:.2f}")

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

# Show the balance only once, after transactions
st.header(f"Updated balance: ${st.session_state.balance:.2f}")
