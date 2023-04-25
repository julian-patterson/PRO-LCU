'''
Julian Patterson 2131249
420-LCU Computer Programming
S. Hilal, instructor
Lab 13
'''
import time


class BankAccount:
    def __init__(self, CODE, NAME, BANK, TYPE, PASSWORD, BALANCE=0):
        self.code = CODE
        self.name = NAME
        self.bank = BANK
        self.type = TYPE
        self.balance = BALANCE
        self.__password = PASSWORD
        self.__last_access = None

    def __repr__(self):
        fmt = "{:6d} {:20s} {:10s} {:10s} {:6d} {:30d}"
        x = fmt.format(self.code, self.name, self.bank,
                       self.type, self.balance, self.__last_access)
        return x

    def withdraw(self, amount):
        if amount <= self.balance:
            print("Your updated balance is: " + (self.balance - amount))
            self.balance -= amount
        else:
            print("You have insufficient funds in your account")
        self.__last_access = time.time()

    def deposit(self, amount):
        self.balance += amount
        print("Your updated balance is: " + self.balance)
        self.__last_access = time.time()

    def transfer(self, other, amount):
        self.balance -= amount
        other.balance += amount
        print("Your money has been to transfered")
        self.__last_access = time.time()

    def get_balance(self):
        print("Your balance is " + self.balance)
        self.__last_access = time.time()

    def create_pwd(self):
        pwd_success = False
        pwd = input("Please input a password: ")
        while pwd_success == False:
            if 8 <= len(pwd) <= 15:
                if pwd.isalnum():
                    if pwd[0].isupper():
                        if pwd[-4].isdigit():
                            if not pwd.isupper():
                                pwd_success = True
                                break
                            else:
                                print(
                                    "Password incorrect; password must have at least one lower case character")
                                return False
                                break
                        else:
                            print(
                                "Password incorrect; last four characters must be a digit")
                            return False
                            break
                    else:
                        print("Password incorrect; first letter must be capitalized")
                        return False
                        break
                else:
                    print("Password incorrect; must be only alphanumeric")
                    return False
                    break
            else:
                print("Password incorrect; must be between [8: 15] characters")
                return False
                break

        if pwd_success == True:
            print("Password Accepted!")
            self.__password = pwd
            return True
        self.__last_access = time.time()

    def verify_pwd(self):
        verify = input("Please enter your password: ")
        if verify == self.__password:
            return True
        if verify != self.__password:
            return False
        self.__last_access = time.time()


# Q1
Accounts = {}

data = open("accounts.txt", "r")

for entry in data.readlines():
    entry.split("\n")
    account = entry.split(",")
    keys = ["name", "bank", "type", "balance"]
    account[-1] = int(account[-1])
    account_dict = dict(zip(keys, account[1:]))
    Accounts[account[0]] = account_dict


# Q2
x = BankAccount(CODE=122156, NAME="Lea Smith",
                BANK="TD", TYPE="Saving", BALANCE=200)

# Q3
BankAccount(CODE=222552, NAME="John Green", BANK="RBC", TYPE="RBC")

# Q4
x.create_pwd("Abcede1234")
