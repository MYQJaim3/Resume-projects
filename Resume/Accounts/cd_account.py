from Accounts import Account

def create_cd_account(balance, interest, months):
    cd_account = Account(balance, interest)
    interest_earned = cd_account.balance * (cd_account.interest/100 * months/12)
    updated_balance = cd_account.balance + interest_earned
    cd_account.set_balance(updated_balance)
    cd_account.set_interest(interest_earned)
    return updated_balance, interest_earned
