class Patient: # Parent Class
    def __init__(self, name, bill_amount): # Initialize the attributes
        self.NAME, self.BILL_AMOUNT = name, bill_amount 
    
    @property 
    def name(self): # Returns the name
        return self.NAME
    
    @name.setter
    def name(self, name): 
        self.NAME = name

    @property
    def bill_amount(self): # Returns the bill amount
        return self.BILL_AMOUNT

    @bill_amount.setter
    def bill_amount(self, bill_amount):
        self.BILL_AMOUNT = bill_amount

    def calculate_bill(self): # returns the bill, which is overridden in the child classes
        return self.BILL_AMOUNT

    def display_patient_type(self): # returns the patient type, which is overridden in the child classes
        return 'Regular Patient'

class SeniorPatient(Patient): # Child Class
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount) # calls out the parent's constructor to inherit the attributes

    def calculate_bill(self): # returns the bill for senior patients with a discount of 20%
        return self.BILL_AMOUNT * 0.8

    def display_patient_type(self): # returns the patient type for senior patients
        return 'Senior Patient'

class PhilhealthPatient(Patient): # Child Class
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount) # calls out the parent's constructor to inherit the attributes

    def calculate_bill(self): # returns the bill for philhealth patients with a discount of 15%
        return self.BILL_AMOUNT * 0.85

    def display_patient_type(self): # returns the patient type for philhealth patients
        return 'Philhealth Member'
        
# Instances
p1 = Patient('Juan Dela Cruz', 15000)
p2 = SeniorPatient('Maria Santos', 15000)
p3 = PhilhealthPatient('Pedro Reyes', 15000)

# Output
print('Hospital Billing System')
print('-'*23)
print(f'Patient Name: {p1.name}\nPatient Type: {p1.display_patient_type()}\nOriginal Bill: ₱{p1.bill_amount:.2f}\nFinal Bill: ₱{p1.calculate_bill():.2f}\n')
print(f'Patient Name: {p2.name}\nPatient Type: {p2.display_patient_type()}\nOriginal Bill: ₱{p2.bill_amount:.2f}\nFinal Bill: ₱{p2.calculate_bill():.2f}\n')
print(f'Patient Name: {p3.name}\nPatient Type: {p3.display_patient_type()}\nOriginal Bill: ₱{p3.bill_amount:.2f}\nFinal Bill: ₱{p3.calculate_bill():.2f}')