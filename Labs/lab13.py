'''
Julian Patterson 2131249
420-LCU Computer Programming
S. Hilal, instructor
Lab 13
'''

class BankAccount:
    def __init__(self, code, name, bank, type, balance, password):
        self.code = code
        self.name = name
        self.bank = bank
        self.type = type
        self.balance = balance
        self.password = password