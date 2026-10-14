crt = 1
class BankAccount:
    account = []
    pos = []

    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    @property
    def account_number(self): # Method
        global crt, pos, accounts
        self.pos.append(crt), self.account.append(self.__account_number)
        crt += 1
        for i in self.account:
            if i == self.__account_number:
                print(f'Account {self.pos[self.account.index(i)]}\nAccount Number: {i}')
                break

    # Sets account number if changed, otherwise it remains the same
    @account_number.setter
    def account_number(self, account_number): # Method
        self.__account_number = account_number

    # Displays Balance
    @property
    def balance(self): # Method
        print(f'Balance: {self.__balance:.2f}')

    # Sets balance with validation to ensure it is not negative
    @balance.setter
    def balance(self, balance): # Method
        print(f'Update balance to {balance}')
        if balance < 0:
            print('The balance must not be a negative number.')
            return
        else:
            self.__balance = balance

BankAccount1 = BankAccount("123456789", 1000)
BankAccount1.account_number
BankAccount1.balance
BankAccount1.account_number = "123467890"
BankAccount1.balance = -100
BankAccount1.account_number
BankAccount1.balance