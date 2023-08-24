class Bank:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = True
    
    def Create_account(self, name, initial_balance):
        account = Account(name, initial_balance)
        self.accounts.append(account)
        self.total_balance += initial_balance
    
    def Check_total_balance(self):
        return self.total_balance
    
    def Check_total_loan_amount(self):
        return self.total_loan_amount
    
    def Toggle_loan_feature(self, status):
        self.loan_feature = status
    
    def Process_loan(self, account):
        if self.loan_feature:
            loan_amount = account.get_balance() * 2
            self.total_loan_amount += loan_amount
            account.deposit(loan_amount)
    
    def Update_total_balance(self, amount):
        self.total_balance += amount
    
class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transaction_history = []
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw: {amount}")
            return True
        else:
            return False
    
    def transfer(self, recipient, amount):
        if self.withdraw(amount):
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
            return True
        else:
            return False
    
    def get_transaction_history(self):
        return self.transaction_history


bank = Bank()
admin = Account("Admin", 100000)
bank.Create_account("Tushar", 5000)

while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transfer\n6. Loan\n7. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter your name: ")
        initial_balance = float(input("Enter initial balance: "))
        bank.Create_account(name, initial_balance)
        print("Account created successfully!")
    
    elif choice == 2:
        name = input("Enter your name: ")
        amount = float(input("Enter the amount to deposit: "))
        account = next((acc for acc in bank.accounts if acc.name == name), None)
        if account:
            account.deposit(amount)
            bank.Update_total_balance(amount)
            print("Amount deposited successfully!")
        else:
            print("Account not found.")
    
    elif choice == 3:
        name = input("Enter your name: ")
        amount = float(input("Enter the amount to withdraw: "))
        account = next((acc for acc in bank.accounts if acc.name == name), None)
        if account:
            if account.withdraw(amount):
                bank.Update_total_balance(-amount)
                print("Amount withdrawn successfully!")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")
    
    elif choice == 4:
        name = input("Enter your name: ")
        account = next((acc for acc in bank.accounts if acc.name == name), None)
        if account:
            print(f"Available balance: {account.get_balance()}")
        else:
            print("Account not found.")
    
    elif choice == 5:
        sender_name = input("Enter your name: ")
        recipient_name = input("Enter recipient's name: ")
        amount = float(input("Enter the amount to transfer: "))
        sender = next((acc for acc in bank.accounts if acc.name == sender_name), None)
        recipient = next((acc for acc in bank.accounts if acc.name == recipient_name), None)
        if sender and recipient:
            if sender.transfer(recipient, amount):
                print("Amount transferred successfully!")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")
    
    elif choice == 6:
        if bank.loan_feature:
            name = input("Enter your name: ")
            account = next((acc for acc in bank.accounts if acc.name == name), None)
            if account:
                bank.process_loan(account)
                print("Loan processed successfully!")
            else:
                print("Account not found.")
        else:
            print("Loan feature is currently disabled by admin.")
    elif choice == 7:
        break
