import random

PRODUCTS = 10
LINE = 0

class Order:
    global PRODUCTS

    def __init__(self, product, payment):
        self.receipt = ''
        self.change = 0
        self.product = product
        self.payment = payment
        self.__current_orders_time = 0
        self.availability = PRODUCTS

    def place_order(self):
        global LINE, PRODUCTS
        count = 0
        if isinstance(self.product, list):
            for ITEM in self.product:
                ITEMS = ['School Supplies', 'Uniform', 'Dinner Meal', 'Lunch Meal', 'Breakfast Meal', 'Snack']
                PRICE = [random.randint(10, 50), random.randint(450, 750), random.randint(75, 110), random.randint(75, 120), random.randint(50, 100), random.randint(20, 70)]
                SPEC = ITEMS.index(ITEM)
                TO_PAY = PRICE[SPEC]
                if ITEM not in ITEMS:
                    return None
                else:
                    if not bool(self.availability):
                        self.availability = random.randint(10, 100)
                        PRODUCTS += self.availability
                        return None
                    else:
                        self.availability -= 1
                        PRODUCTS -= 1
                        if self.payment - count > TO_PAY:
                            count += TO_PAY
                        else:
                            return None
            self.change = self.payment - count
            self.receipt = f'Receipt:\nOrdered Items: {", ".join(self.product)}\nPayment: {self.payment}\nTotal Cost: {count}\nChange: {self.change}'
            LINE += 1
        else:
            ITEMS = ['School Supplies', 'Uniform', 'Dinner Meal', 'Lunch Meal', 'Breakfast Meal', 'Snack']
            PRICE = [random.randint(10, 50), random.randint(450, 750), random.randint(75, 110), random.randint(75, 120), random.randint(50, 100), random.randint(20, 70)]
            SPEC = ITEMS.index(self.product)
            TO_PAY = PRICE[SPEC]
            if self.product not in ITEMS:
                return None
            else:
                if not bool(self.availability):
                    self.availability = random.randint(10, 100)
                    PRODUCTS += self.availability
                    return None
                else:
                    self.availability -= 1
                    PRODUCTS -= 1
                    if self.payment - count > TO_PAY:
                        count += TO_PAY
                    else:
                        return None
            self.change = self.payment - count
            self.receipt = f'Receipt:\nOrdered Items: {self.product}\nPayment: {self.payment}\nTotal Cost: {count}\nChange: {self.change}'
            LINE += 1
        self.__current_orders_time = sum(len(item) for item in self.product.split()) if isinstance(self.product, str) else sum(len(item) for item in self.product)

    def check_receipt(self):
        if self.receipt:
            return self.receipt
        else:
            return 'No receipt available. Product may not be available or payment is insufficient.'

    def line_up(self):
        self.__current_orders_time *= LINE
        return f'{self.__current_orders_time:.2f} seconds'

    def receive_order(self):
        if self.receipt:
            LINE -= 1
            return f'Received: {self.product if isinstance(self.product, str) else ", ".join(self.product)}'
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
                self.products_punched = len(object.product) 
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

    ID0204 = Order(['Breakfast Meal', 'Lunch Meal', 'Dinner Meal'], 400)
    ID0408 = Order('Uniform', 1000)
    ID0612 = Order(['Snack', 'Dinner Meal'], 500)
    COUNTER = Counter()

    print('------ BEFORE RELATIONSHIP ------')
    print('\nCounter')
    print('\nOrder ID 0204')
    print(COUNTER.check_cash(ID0204))
    COUNTER.remaining_products()
    print(COUNTER.calculate_rate(ID0204))

    print('\nOrder ID 0408')
    print(COUNTER.check_cash(ID0408))
    COUNTER.remaining_products()
    print(COUNTER.calculate_rate(ID0408))

    print('\nOrder ID 0612')
    print(COUNTER.check_cash(ID0612))
    COUNTER.remaining_products()
    print(COUNTER.calculate_rate(ID0612))

    print('\n------ BUILDING RELATIONSHIP ------')
    print('\nOrder ID 0204')
    ID0204.place_order()
    print(ID0204.check_receipt())

    print('\nOrder ID 0408')
    ID0408.place_order()
    print(ID0408.check_receipt())

    print('\nOrder ID 0612')
    ID0612.place_order()
    print(ID0612.check_receipt())

    print('\n------ AFTER RELATIONSHIP ------')
    print('\nCounter')
    print('\nOrder ID 0204')
    print(COUNTER.check_cash(ID0204))
    COUNTER.remaining_products()
    print(COUNTER.calculate_rate(ID0204))

    print('\nOrder ID 0408')
    print(COUNTER.check_cash(ID0408))
    COUNTER.remaining_products()
    print(COUNTER.calculate_rate(ID0408))

    print('\nOrder ID 0612')
    print(COUNTER.check_cash(ID0612))
    COUNTER.remaining_products()
    print(COUNTER.calculate_rate(ID0612))

    print('\nRelated object(s)\nChange\nCost\nPayment\nProduct')