"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        return self.contract.calculate_pay() + (self.commission.calculate_pay() if self.commission else 0)
    
    def __str__(self):
        contract_str = str(self.contract)
        commission_str = f" and receives a {self.commission}" if self.commission else ''
        return f"{self.name} works on a {contract_str}{commission_str}. Their total pay is {self.get_pay()}."

class Contract:
    def calculate_pay(self):
        pass

    def __str__(self):
        pass

class SalaryContract(Contract):
    def __init__(self, salary):
        self.salary = salary

    def calculate_pay(self):
        return self.salary

    def __str__(self):
        return f"monthly salary of {self.salary}"

class HourlyContract(Contract):
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate

    def __str__(self):
        return f"contract of {self.hours_worked} hours at {self.hourly_rate}/hour"

class Commission:
    def calculate_pay(self):
        pass

    def __str__(self):
        pass

class BonusCommission(Commission):
    def __init__(self, bonus):
        self.bonus = bonus

    def calculate_pay(self):
        return self.bonus

    def __str__(self):
        return f"bonus commission of {self.bonus}"

class ContractCommission(Commission):
    def __init__(self, contracts_landed, commission_per_contract):
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def calculate_pay(self):
        return self.contracts_landed * self.commission_per_contract

    def __str__(self):
        return f"commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract"

# Creating employee instances
billie = Employee("Billie", SalaryContract(4000))
charlie = Employee("Charlie", HourlyContract(100, 25))
renee = Employee("Renee", SalaryContract(3000), ContractCommission(4, 200))
jan = Employee("Jan", HourlyContract(150, 25), ContractCommission(3, 220))
robbie = Employee("Robbie", SalaryContract(2000), BonusCommission(1500))
ariel = Employee("Ariel", HourlyContract(120, 30), BonusCommission(600))

