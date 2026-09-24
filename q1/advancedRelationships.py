import random

PRODUCTS = 10
LINE = 0

class Transaction:
    def __init__(self, offer, payment):
        self.payment = payment
        self.offer = offer
        self.cost = 0
        if isinstance(self.offer, list):
            for self.ITEM in self.offer:
                self.ITEMS = ['School Supplies', 'Uniform', 'Dinner Meal', 'Lunch Meal', 'Breakfast Meal', 'Snack']
                self.PRICE = [random.randint(10, 50), random.randint(450, 750), random.randint(75, 110), random.randint(75, 120), random.randint(50, 100), random.randint(20, 70)]
                self.SPEC = self.ITEMS.index(self.ITEM)
                self.TO_PAY = self.PRICE[self.SPEC]
                if self.payment - self.cost > self.TO_PAY:
                    self.cost += self.TO_PAY
        else:
            self.ITEMS = ['School Supplies', 'Uniform', 'Dinner Meal', 'Lunch Meal', 'Breakfast Meal', 'Snack']
            self.PRICE = [random.randint(10, 50), random.randint(450, 750), random.randint(75, 110), random.randint(75, 120), random.randint(50, 100), random.randint(20, 70)]
            self.SPEC = self.ITEMS.index(self.offer)
            self.TO_PAY = self.PRICE[self.SPEC]
            if self.payment - self.cost > self.TO_PAY:
                self.cost += self.TO_PAY
        self.change = self.payment - self.cost

    def transact():
        pass
        
# Inherited class Transaction's attributes (made major changes in Order)
class Order(Transaction):
    global PRODUCTS

    def __init__(self, offer, payment):
        super().__init__(offer, payment)
        self.receipt = ''
        self.__current_orders_time = 0
        self.availability = PRODUCTS

    # modified transact
    def transact(self):
        global PRODUCTS, LINE
        if self.cost == 0 or self.payment < self.cost:
            return None
        if isinstance(self.offer, list):
            for ITEM in self.offer:
                if ITEM not in self.ITEMS:
                    return None
                if not bool(self.availability) or self.availability < len(self.offer):
                    self.availability = random.randint(10, 100)
                    PRODUCTS += self.availability
                    return None
            self.availability -= len(self.offer)
            PRODUCTS -= len(self.offer)
            self.receipt = f'Receipt:\nOrdered Items: {", ".join(self.offer)}\nPayment: {self.payment}\nTotal Cost: {self.cost}\nChange: {self.change}'
            LINE += 1
        else:
            if self.offer not in self.ITEMS:
                return None
            if not bool(self.availability) or self.availability < 1:
                self.availability = random.randint(10, 100)
                PRODUCTS += self.availability
                return None
            self.availability -= 1
            PRODUCTS -= 1
            self.receipt = f'Receipt:\nOrdered Items: {self.offer}\nPayment: {self.payment}\nTotal Cost: {self.cost}\nChange: {self.change}'
            LINE += 1
        self.__current_orders_time = sum(len(item) for item in self.offer.split()) if isinstance(self.offer, str) else sum(len(item) for item in self.offer)


    def check_receipt(self):
        if self.receipt:
            return self.receipt
        else:
            return 'No receipt available. Product may not be available or payment is insufficient.'

    def line_up(self):
        self.__current_orders_time *= LINE
        return f'{self.__current_orders_time:.2f} seconds'

    def receive_order(self):
        global LINE
        if self.receipt:
            LINE -= 1
            return f'Received: {self.offer if isinstance(self.offer, str) else ", ".join(self.offer)}'
        else:
            return None
    
class Counter:
    def __init__(self):
        self.orders_done, self.products_punched, self.income = 0, 0, 0

    def check_cash(self, object):
        try:
            expense = object.payment - object.change
            self.income = expense
            return f'The income from the order ID is {self.income}.'
        except ValueError:
            return None

    def calculate_rate(self, object):
        try:
            if type(object.product) is list:
                self.products_punched = len(object.offer) 
                expense = object.payment - object.change
                self.income = expense
                rate = f'The rate is PHP {(self.income / self.products_punched):.2f} per product bought.'
                return rate
            else:
                expense = object.payment - object.change
                self.income = expense
                rate = f'The rate is PHP {self.income:.2f} per product bought.'
                return rate
        except ValueError:
            return None

    def remaining_products(self):
        return PRODUCTS

if __name__ == '__main__':
    _0816 = Transaction('Breakfast Meal', 200)
    ID0816 = Order('Breakfast Meal', 200)
    ID1020 = Order('School Supplies', 100)
    counter = Counter()
    ID0816.transact()
    ID1020.transact()
    print('\nUsed module Random; parent object and child object might have different results despite having the same inputs.\n')
    print(f'Parent attribute:\nOffer = {_0816.offer}\nPayment = {_0816.payment}\nCost = {_0816.cost}\nChange = {_0816.change}\n')
    print(f'Child attribute:\nOffer = {ID0816.offer}\nPayment = {ID0816.payment}\nCost = {ID0816.cost}\nChange = {ID0816.change}\n')
    print(f'Counter contains 2 Orders:\nOrder ID 0816\n{counter.check_cash(ID0816)}\n\nOrder ID 1020\n{counter.check_cash(ID1020)}')