
class BankAccount:
    account = []
    pos = []
    crt = 1

    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute
        self.account.append(account_number), self.pos.append(self.crt)

    @property
    def account_number(self): # Getter Method
        global crt, pos, account
        for i in self.account:
            if i == self.__account_number:
                print(f'Account {self.pos[self.account.index(i)]}\nAccount Number: {i}')
                break

    # Sets account number if changed, otherwise it remains the same
    @account_number.setter
    def account_number(self, account_number): # Setter Method
        global crt, pos, account
        for i in self.account:
            if i == self.__account_number:
                self.account.remove(i), self.pos.remove(self.crt)
                self.__account_number = account_number
                self.account.append(account_number), self.pos.append(self.crt)
                self.crt -= 1
        self.crt += 1
        self.__account_number = account_number

    # Displays Balance
    @property
    def balance(self): # Getter Method
        print(f'Balance: {self.__balance:.2f}')

    # Sets balance with validation to ensure it is not negative
    @balance.setter
    def balance(self, balance): # Setter Method
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