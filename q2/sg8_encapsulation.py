crt = 1
class BankAccount:

    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    # Sets account number if changed, otherwise it remains the same
    def set_account_number(self, account_number): # Method
        self.__account_number = account_number

    # Sets balance with validation to ensure it is not negative
    def set_balance(self, balance): # Method
        print(f'Update balance to {balance}')
        if balance < 0:
            print('The balance must not be a negative number.')
            return
        else:
            self.__balance = balance

    # Complex listing for arranging account number
    def get_account_number(self): # Method
        global crt
        accounts = []
        pos = []
        pos.append(crt), accounts.append(self.__account_number)
        crt += 1
        for i in accounts:
            if i == self.__account_number:
                print(f'Account {pos[accounts.index(i)]}\nAccount Number: {i}')
                break

    # Displays Balance
    def get_balance(self): # Method
        print(f'Balance: {self.__balance:.2f}')

BankAccount1 = BankAccount("123456789", 1000)
BankAccount1.get_account_number()
BankAccount1.get_balance()
BankAccount1.set_account_number("123456789")
BankAccount1.set_balance(- 100)
BankAccount1.get_account_number()
BankAccount1.get_balance()