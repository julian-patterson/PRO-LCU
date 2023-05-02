'''
Julian Patterson 2131249
420-LCU Computer Programming
S. Hilal, instructor
Lab 13
'''
import datetime


class BankAccount:
    def __init__(self, CODE, NAME, BANK, TYPE, BALANCE=0):
        self.code = CODE
        self.name = NAME
        self.bank = BANK
        self.type = TYPE
        self.balance = BALANCE
        self.__password = None
        self.__last_access = datetime.datetime.now()

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
        self.__last_access = datetime.datetime.now()

    def deposit(self, amount):
        self.balance += amount
        print("Your updated balance is: " + str(self.balance))
        self.__last_access = datetime.datetime.now()

    def transfer(self, other, amount):
        self.balance -= amount
        other.balance += amount
        print("Your money has been to transfered")
        self.__last_access = datetime.datetime.now()

    def get_balance(self):
        print("Your balance is " + self.balance)
        self.__last_access = datetime.datetime.now()

    def create_pwd(self):
        print(str(self.name))
        pwd_success = False
        pwd = input("Please input a password: ")
        if 8 <= len(pwd) <= 15:
            if pwd.isalnum():
                if pwd[0].isupper():
                    if pwd[-4].isdigit():
                        if not pwd.isupper():
                            pwd_success = True

                        else:
                            print(
                                "Password incorrect; password must have at least one lower case character")
                            return False

                    else:
                        print(
                            "Password incorrect; last four characters must be a digit")
                        return False

                else:
                    print("Password incorrect; first letter must be capitalized")
                    return False

            else:
                print("Password incorrect; must be only alphanumeric")
                return False

        else:
            print("Password incorrect; must be between [8: 15] characters")
            return False

        if pwd_success == True:
            print("Password Accepted!")
            self.__password = pwd
            return True
        self.__last_access = datetime.datetime.now()

    def verify_pwd(self):
        print(self.name)
        verify = input("Please enter your password: ")
        if self.__password == None:
            print("You must create a password and then you may retry! \n")
            self.create_pwd()
        elif verify == self.__password:
            return True
        elif verify != self.__password:
            return False
        self.__last_access = datetime.datetime.now()


# Q1
Accounts = {}

data = open("accounts.txt", "r")

for entry in data.readlines():
    entry.split("\n")
    account = entry.split(",")
    keys = ["name", "bank", "type", "balance"]
    account[-1] = int(account[-1])
    account_dict = dict(zip(keys, account[1:]))
    Accounts[int(account[0])] = account_dict

print(Accounts)

# Q2
lea_smith = BankAccount(CODE=122156, NAME="Lea Smith",
                        BANK="TD", TYPE="Saving", BALANCE=200)
Accounts[lea_smith.code] = {"name": lea_smith.name, "bank": lea_smith.bank,
                            "type": lea_smith.type, "balance": lea_smith.balance}

# Q3
john_green = BankAccount(
    CODE=222552, NAME="John Green", BANK="RBC", TYPE="RBC")
Accounts[john_green.code] = {"name": john_green.name, "bank": john_green.bank,
                             "type": john_green.type, "balance": john_green.balance}


# Q4
lea_smith.create_pwd()

# Q5
for key, value in Accounts.items():
    if key == 122156:
        BankAccount(CODE=key, NAME=value["name"], BANK=value["bank"],
                    TYPE=value["type"], BALANCE=value["balance"]).verify_pwd()
        BankAccount(CODE=key, NAME=value["name"], BANK=value["bank"],
                    TYPE=value["type"], BALANCE=value["balance"]).deposit(100)
        print(BankAccount(
            CODE=key, NAME=value["name"], BANK=value["bank"], TYPE=value["type"], BALANCE=value["balance"]))
    else:
        continue


# Q6
for key in Accounts:
    if key == 888888:
        BankAccount.verify_pwd(888888)
        BankAccount.deposit(888888, 100)
    else:
        print("This account does not exist")

# Q7
for key in Accounts:
    if key == 122156:
        BankAccount.verify_pwd(122156)
        BankAccount.withdraw(122156, 100)
    else:
        print("This account does not exist")

# Q8
for key in Accounts:
    if key == 122156:
        BankAccount.verify_pwd(122156)
        BankAccount.get_balance(122156)
    else:
        print("This account does not exist")

# Q9
fmt = "{:6s} {:20s} {:10s} {:10s} {:30s}"
print(fmt.format("CODE" + "NAME" + "BANK" + "TYPE" + "BALANCE"))
for key, value in Accounts.items():
    print("{:6d}".format(key) + "{:20s}".format(str(value["name"])) + "{:10s}".format(str(
        value["bank"])) + "{:10s}".format(str(value["type"])) + "{:30s}".format(str(value["balance"])))
