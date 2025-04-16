from Accounts import Account

def create_savings_account(balance, interest, months):
    savings_account = Account(balance, interest)
    interest_earned = savings_account.balance * (savings_account.interest/100 * months/12)
    updated_balance = savings_account.balance + interest_earned
    savings_account.set_balance(updated_balance)
    savings_account.set_interest(interest_earned)
    return updated_balance, interest_earned
