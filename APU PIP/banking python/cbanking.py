from random import randint
from datetime import date
class BankingSystem:
    def __init__(self):
        self.user_account = {}
        self.user_account_balance = {}
        self.admin_account = {}
        self.transaction_history = {}
        #self.iin = 400000

    def main_welcom_screen(self):
            print(
                "1. User Account Login\n"
                "2. Admin Login\n"
                "3. Create Admin\n"
                "0. Exit"
            )
            main_menu_selection = str(input())
            if main_menu_selection == "1":
                self.user_login()
            if main_menu_selection == "2":
                self.admin_login()
                #self.account_login()
            if main_menu_selection == "3":
                self.create_admin()
            if main_menu_selection == "0":
                print("\n")
                return "Bye!"

    def create_admin(self):
        admin_username = f"admin{randint(0000, 9999)}"
        admin_password = format(randint(0000, 9999), '04d')
        self.admin_account[admin_username] = admin_password

        print("\n")
        print("Admin Account has been created")
        print("Admin Username:")
        print(admin_username)
        print("Admin Password:")
        print(admin_password)
        print("\n")
        self.main_welcom_screen()
    
    def admin_login(self):
        print("\n")
        print("Enter Admin Username:")
        entered_admin_username = str(input())

        print("Enter Password:")
        entered_admin_password = str(input())
        print("\n")

        if entered_admin_username in self.admin_account:
            correct_password = self.admin_account[entered_admin_username]
            if entered_admin_password == correct_password:
                print("Admin Succesfully Login")
                self.admin_panel()
            else:
                print("Password is Wrong")
                self.main_welcom_screen()
        else:
            print("Admin Account Do Not Exist!")
            print("\n")
            self.main_welcom_screen()
    
    def admin_panel(self):
        print(
            "\n1. Create Account For User\n"
            "2. View All Customer Profile\n"
            "3. Search Specific Customer\n"
            "4. Log out\n"
            "0. Exit"
        )
        admin_selection = str(input())
        if admin_selection == "1":
            print("\n")
            self.create_account()
        
        elif admin_selection == "2":
            self.view_all_customer_profile()

        elif admin_selection == "3":
            self.search_customer()

        elif admin_selection == "4":
            print("\n")
            print("You have successfully logged out!")
            print("\n")
            self.main_welcom_screen()

        elif admin_selection == "0":
            print("\n")
            print("Bye!")
    
    def create_account(self):
        user_username = f"user{randint(0000, 9999)}"
        user_password = format(randint(0000, 9999), '04d')
        self.user_account[user_username] = user_password
        self.user_account_balance[user_username] = 20
        self.transaction_history[user_username] = []
        print("\n")
        print("User Account has been created")
        print("User Username:")
        print(user_username)
        print("User Password:")
        print(user_password)
        print(f"Default Balance: {self.user_account_balance[user_username]}")
        print("\n")
        self.admin_panel()
    
    def view_all_customer_profile(self):
        print(self.user_account_balance)
        for key, value in self.user_account_balance.items():
            print(f'User: {key}, Balance: {value}')
        self.admin_panel()
    
    def search_customer(self):
        print('\n')
        print("Insert the username you want to search")
        input_username = str(input())
        if input_username in self.user_account:
            print(f'Username: {input_username}')
            print(f'Password: {self.user_account[input_username]}')
            print(f'Balance: {self.user_account_balance[input_username]}')
            print('History: ')
            for each in self.transaction_history[input_username]:
                print(each)
            self.admin_panel()
        else:
            print("Username do not exist")
            self.admin_panel()

    def user_login(self):
        print("\n")
        print("Enter your username:")
        username_entered = str(input())
        print("Enter your password:")
        password_entered = str(input())
        print("\n")

        if username_entered in self.user_account:
            correct_password = self.user_account[username_entered]
            if password_entered == correct_password:
                print("Successful Login")
                print("\n")
                self.user_panel(username_entered)
            else:
                print("Your Password is Wrong")
                print("\n")
                self.main_welcom_screen()
        else:
            print("Username does not exist")
            print("\n")
            self.main_welcom_screen()

    def user_panel(self, username):
        print(
            "\n1. Check Balance\n"
            "2. Deposit\n"
            "3. Withdraw\n"
            "4. Transaction History\n"
            "5. Log out\n"
            "0. Exit"
        )
        user_selection = str(input())

        if user_selection == "1":
            print("\n")
            print(f"User: {username}")
            print(f"Your Balance: {self.user_account_balance[username]}")
            self.user_panel(username)
        
        elif user_selection == "2":
            self.deposit_cash(username)
        elif user_selection == "3":
            self.withdraw_cash(username)
        elif user_selection == "4":
            self.view_history(username)
        elif user_selection == "5":
            print("\n")
            print("You have successfully logged out!")
            print("\n")
            self.main_welcom_screen()

        elif user_selection == "0":
            print("\n")
            print("Bye!")
        
    def deposit_cash(self, username):
        print("\n")
        print("Enter the amount you want to deposit")
        try:
            amount = int(input())
            if amount <= 0:
                print("Amount deposit cannot be 0 or negative !")
                self.user_panel(username)
            else:
                self.user_account_balance[username] += amount
                today = date.today()
                today_formatted = today.strftime("%d/%m/%Y")
                this_history = f'DEPOSIT at {today_formatted} - You had deposit {amount}'
                self.transaction_history[username].append(this_history)
                print(f"You had successfully deposit {amount}")
                print(f"Your balance is now {self.user_account_balance[username]}")
                self.user_panel(username)
        except:
            print("Please enter number only")
            self.deposit_cash(username)

    def withdraw_cash(self, username):
        print("\n")
        print("Enter the amount you want to withdraw")
        try:
            amount = int(input())
            if amount > self.user_account_balance[username]:
                print(f"You want to withdraw {amount}, but your balance has only {self.user_account_balance[username]} !")
                self.withdraw_cash(username)
            elif amount <= 0:
                print("Amount withdraw cannot be 0 or negative !")
                self.user_panel(username)
            else:
                self.user_account_balance[username] -= amount
                today = date.today()
                today_formatted = today.strftime("%d/%m/%Y")
                this_history = f'WITHDRAW at {today_formatted} - You had withdraw {amount}'
                self.transaction_history[username].append(this_history)
                print(f"You had successfully withdraw {amount}")
                print(f"Your balance is now {self.user_account_balance[username]}")
                self.user_panel(username)
        except:
            print("Please enter number only")
            self.deposit_cash(username)
    
    def view_history(self, username):
        print('\n')
        historys = self.transaction_history[username]
        if not historys:
            print("You have yet do any transaction")
            self.user_panel(username)
        else:
            for history in historys:
                print(history)
            self.user_panel(username)

print(BankingSystem().main_welcom_screen())