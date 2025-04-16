from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    savings_balance = float(input("Enter the savings balance: "))
    savings_interest = float(input("Enter the savings interest rate: "))
    savings_months = int(input("Enter the number of months for the savings account: "))
    savings_updated_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_months)
    print(f"Savings Account: Interest Earned = {savings_interest_earned:.2f}, Updated Balance = {savings_updated_balance:.2f}")

    cd_balance = float(input("Enter the CD balance: "))
    cd_interest = float(input("Enter the CD interest rate: "))
    cd_months = int(input("Enter the number of months for the CD account: "))
    cd_updated_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_months)
    print(f"CD Account: Interest Earned = {cd_interest_earned:.2f}, Updated Balance = {cd_updated_balance:.2f}")

if __name__ == "__main__":
    main()
