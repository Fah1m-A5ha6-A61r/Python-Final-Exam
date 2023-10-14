class Bank:
    def __init__(self):
        self.users = []
        self.admin_logged_in = False
        self.bank_balance = 100000  # Initial bank balance
        self.loan_feature_enabled = True
        self.bankrupt = False

    def admin_login(self, admin_name, password):
        if admin_name == "ADMIN" and password == "123":
            self.admin_logged_in = True
            print("\nAdmin logged in successfully.")
        else:
            print("\nInvalid admin credentials.")

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        print(f"\nAccount created for {name} with account number {user.account_number}")

    def delete_account(self, account_number):
        if self.admin_logged_in:
            for user in self.users:
                if user.account_number == account_number:
                    self.users.remove(user)
                    print(f"\nAccount {account_number} deleted.")
                    return
            print(f"\nAccount {account_number} not found.")
        else:
            print("Admin must be logged in to delete an account.")

    def show_user_accounts(self):
        if self.admin_logged_in:
            print(f"\nThere are currently {len(self.users)} users in your bank.\n")
            for user in self.users:
                user.display_info()
        else:
            print("\nAdmin must be logged in to view user accounts.")

    def total_available_balance(self):
        if self.admin_logged_in:
            total_balance = sum(user.balance for user in self.users)
            print(f"\nTotal available balance: {total_balance}")
        else:
            print("\nAdmin must be logged in to check total available balance.")

    def total_loan_amount(self):
        if self.admin_logged_in:
            total_loans = sum(user.loan for user in self.users)
            print(f"\nTotal loan amount: {total_loans}")
        else:
            print("\nAdmin must be logged in to check total loan amount.")

    def toggle_loan_feature(self):
        if self.admin_logged_in:
            self.loan_feature_enabled = not self.loan_feature_enabled
            status = "enabled" if self.loan_feature_enabled else "disabled"
            print(f"\nLoan feature is now {status}.")
        else:
            print("\nAdmin must be logged in to toggle the loan feature.")

    def declare_bankruptcy(self, is_bankrupt):
        if self.admin_logged_in:
            self.bankrupt = is_bankrupt
            status = "bankrupt" if is_bankrupt else "solvent"
            print(f"\nThe bank is now declared as {status}.")
        else:
            print("\nAdmin must be logged in to declare the bank's status.")


class User:
    account_number_counter = 1  # Initial account number
    transaction_history = []
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = User.account_number_counter
        User.account_number_counter += 1
        self.balance = 0
        self.loan = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nDeposited ${amount}. New balance: ${self.balance}")
            User.transaction_history.append(f"Deposited ${amount}")
        else:
            print("\nInvalid deposit amount.")

    def withdraw(self, amount):
        if bank.bankrupt == True:
            print("\nFailed to withdraw as Bank is now Bankrupt")
        else:
            if self.balance >= amount:
                self.balance -= amount
                print(f"\nWithdrew ${amount}. New balance: ${self.balance}")
                User.transaction_history.append(f"Withdrawn ${amount}")
            else:
                print("\nWithdrawal amount exceeded.")

    def check_balance(self):
        print(f"\nAvailable balance: ${self.balance}")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            print(f"\nTransferred ${amount} to account {recipient.account_number}.")
            User.transaction_history.append(f"Transferred ${amount} to account {recipient.account_number}")
        else:
            print("\nInsufficient funds for the transfer.")

    def take_loan(self, amount):
        if self.loan < 2 and amount > 0 and bank.loan_feature_enabled:
            self.loan += 1
            self.balance += amount
            print(f"\nLoan taken: ${amount}. New balance: ${self.balance}")
            User.transaction_history.append(f"Loan taken: ${amount}")
        elif self.loan >= 2:
            print("\nYou have reached the maximum number of loans.")
        elif not bank.loan_feature_enabled:
            print("\nLoan feature is currently disabled.")
        else:
            print("\nInvalid loan request.")

    def display_info(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ${self.balance}")
        print(f"Loan Count: {self.loan}\n")

    def show_transaction_history(self):
        for h in User.transaction_history:
            print(h)    


bank = Bank()

while True:
    print("\nWelcome to the Banking Management System")
    print("1. Admin Login")
    print("2. User")
    print("3. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        admin_name = input("Enter Admin Name: ")
        admin_password = input("Enter Password: ")
        bank.admin_login(admin_name, admin_password)
        while True:
            print("\nAdmin Menu")
            print("1. Create an Account")
            print("2. Delete an account")
            print("3. See all accounts")
            print("4. Total Bank Balance")
            print("5. Toggle Loan Feature")
            print("6. Update Bank Status")
            print("7. Log Out")
            admin_choice = input("Select an option: ")
            if admin_choice == "1":
                name = input("Enter your name: ")
                email = input("Enter your mail: ")
                adrs = input("Enter your address: ")
                Actype = input("Account type : ")
                bank.create_account(name,email,adrs,Actype)
            elif admin_choice == "2":
                dlt_acc_num = int(input("Enter Account Number: "))
                bank.delete_account(dlt_acc_num)
            elif admin_choice == "3":
                bank.show_user_accounts()
            elif admin_choice == "4":
                bank.total_available_balance()                              
            elif admin_choice == "5":
                bank.toggle_loan_feature()                              
            elif admin_choice == "6":
                ch3 = input("\nIs the bank bankrupt? (type 1 if yes otherwise type anything other than 1): ")
                if ch3 == 1:
                    bank.declare_bankruptcy(True)
                else:
                    bank.declare_bankruptcy(False)                              
            else:
                bank.admin_logged_in = False
                break

    elif choice == "2":
        ch2 = input("\nRegister or login (type R / L) : ")
        if ch2 == 'R':
            name = input("Enter your name: ")
            email = input("Enter your mail: ")
            adrs = input("Enter your address: ")
            Actype = input("Account type : ")
            bank.create_account(name,email,adrs,Actype)
        else:    
            user_account_number = int(input("Enter your account number: "))
            CurrentUser = None
            for u in bank.users:
                if u.account_number == user_account_number:
                    CurrentUser = u
                    break
            if CurrentUser:
                while True:
                    print(f"\nUser Menu - Welcome! {CurrentUser.name}")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Status")
                    print("4. Transfer Money")
                    print("5. Take a Loan")
                    print("6. Transaction History")
                    print("7. Log Out")
                    user_choice = input("Select an option: ")

                    if user_choice == "1":
                        amount = float(input("Enter the deposit amount: $"))
                        CurrentUser.deposit(amount)
                    elif user_choice == "2":
                        amount = float(input("Enter the withdrawal amount: $"))
                        CurrentUser.withdraw(amount)
                    elif user_choice == "3":
                        CurrentUser.display_info()
                    elif user_choice == "4":
                        recipient_account_number = int(input("Enter the recipient's account number: "))
                        recipient = None
                        for u in bank.users:
                            if u.account_number == recipient_account_number:
                                recipient = u
                                break
                        if recipient:
                            amount = float(input("Enter the transfer amount: $"))
                            CurrentUser.transfer(recipient, amount)
                        else:
                            print("\nRecipient account does not exist.")
                    elif user_choice == "5":
                        amount = float(input("Enter the loan amount: $"))
                        CurrentUser.take_loan(amount)
                    elif user_choice == "6":
                        print(f"\nThis is your transaction history till now {CurrentUser.name}\n")
                        CurrentUser.show_transaction_history()
                    elif user_choice == "7":
                        CurrentUser = None
                        break
                    else:
                        print("\nInvalid option.")
            else:
                print("\nUser account not found.")

    elif choice == "3":
        break
    else:
        print("\nInvalid option.")

