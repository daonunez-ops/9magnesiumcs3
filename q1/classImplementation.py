import random
class Order:
    def __init__(self, product, payment):
        self.receipt = ''
        self.change = 0
        self.product = product
        self.payment = payment
        self.__current_orders_time = 0
    def place_order(self):
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
                    BOOL = [True, False]
                    IS_AVAILABLE = random.choice(BOOL)
                    if not IS_AVAILABLE:
                        return None
                    else:
                        if self.payment - count > TO_PAY:
                            count += TO_PAY
                        else:
                            return None
            self.change = self.payment - count
            self.receipt = f'Receipt:\nOrdered Items: {", ".join(self.product)}\nPayment: {self.payment}\nTotal Cost: {count}\nChange: {self.change}'
        else:
            ITEMS = ['School Supplies', 'Uniform', 'Dinner Meal', 'Lunch Meal', 'Breakfast Meal', 'Snack']
            PRICE = [random.randint(10, 50), random.randint(450, 750), random.randint(75, 110), random.randint(75, 120), random.randint(50, 100), random.randint(20, 70)]
            SPEC = ITEMS.index(self.product)
            TO_PAY = PRICE[SPEC]
            if self.product not in ITEMS:
                return None
            else:
                BOOL = [True, False]
                IS_AVAILABLE = random.choice(BOOL)
                if not IS_AVAILABLE:
                    return None
                else:
                    if self.payment - count > TO_PAY:
                        count += TO_PAY
                    else:
                        return None
            self.change = self.payment - count
            self.receipt = f'Receipt:\nOrdered Items: {self.product}\nPayment: {self.payment}\nTotal Cost: {count}\nChange: {self.change}'
        self.__current_orders_time = sum(len(item) for item in self.product.split()) if isinstance(self.product, str) else sum(len(item) for item in self.product)
    def check_receipt(self):
        if self.receipt:
            print(self.receipt)
        else:
            print('No receipt available. Product may not be available or payment is insufficient.')
    def line_up(self):
        in_line = round(random.uniform(1, 10), 2)
        self.__current_orders_time *= in_line
        print(f'{self.__current_orders_time:.2f} seconds')
    def receive_order(self):
        if self.receipt:
            print(f'Received: {self.product if isinstance(self.product, str) else ", ".join(self.product)}')
        else:
            return None

if __name__ == "__main__":
    order1 = Order(['School Supplies', 'Lunch Meal'], 1000)
    order2 = Order('Uniform', 1000)
    print('\n----- BEFORE -----')
    print('\nObject 1:')
    order1.place_order()
    order1.check_receipt()
    print('\nObject 2:')
    order2.check_receipt()
    print('----- AFTER -----')
    print('\nObject 1:')
    order1.place_order()
    order1.check_receipt()
    order1.line_up()
    order1.receive_order()
    print('\nObject 2:')
    order2.check_receipt()