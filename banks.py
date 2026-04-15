import pickle

numberOfAccounts = 0
id = None
FILE_NAME = "bank.dat"
countOfAccounts = "account.dat"
customer = []

class Bank:
    def __init__(self, balance, age, accountnumber, name):
        self.balance = balance
        self.age = age
        self.accountnumber = accountnumber
        self.name = name

def customerDetails():
    with open("Bank_details.txt", "a") as details:
        for cust in customer:
            details.write("-------CUSTOMER ID-----\n")
            details.write(f"Customer Account Number is {cust.accountnumber}\n")
            details.write(f"Customer Name is {cust.name}\n")
            details.write(f"Customer Age is {cust.age}\n")
            details.write(f"Customer Balance is {cust.balance}\n\n")

def openAccount():
    global numberOfAccounts
    if numberOfAccounts >= 100:
        print("Cannot open more accounts. The bank is full.")
        return

    accountnumber = int(input("Your account number: "))
    if any(cust.accountnumber == accountnumber for cust in customer):
        print("Account number already exists. Choose another account number.")
        openAccount()
        return

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    balance = int(input("Enter how much you want to deposit: "))

    new_customer = Bank(balance, age, accountnumber, name)
    customer.append(new_customer)
    numberOfAccounts += 1

def checkAccount(): 
    global id
    accountNumber = int(input("Enter your account number: "))
    for i, cust in enumerate(customer):
        if cust.accountnumber == accountNumber:
            id = i
            return True
    return False

def depositMoney():
    result = checkAccount()
    if result:
        deposit1 = int(input("How much you want to deposit: "))
        customer[id].balance += deposit1
        print(f"Your balance is {customer[id].balance}")
    else:
        print("Account does not found")

def withdrawMoney():
    result = checkAccount()
    if result:
        withdraw = int(input("How much you want to withdraw: "))
        if customer[id].balance < withdraw:
            print("You don't have sufficient balance in your account")
        else:
            customer[id].balance -= withdraw
            print(f"Your balance is {customer[id].balance}")
    else:
        print("Account does not found")

def printAccountInfo():
    result = checkAccount()
    if result:
        print(f"Name of account holder is {customer[id].name}")
        print(f"Age of account holder is {customer[id].age}")
        print(f"Balance of this account is {customer[id].balance}")
    else:
        print("Account does not found")

def deleteAccount():
    global numberOfAccounts
    result = checkAccount()
    if result:
        del customer[id]
        numberOfAccounts -= 1
        print("Account deleted successfully.")
    else:
        print("Account does not found")

def write():
    with open(countOfAccounts, 'wb') as file:
        pickle.dump(numberOfAccounts, file)

    with open(FILE_NAME, 'wb') as file:
        pickle.dump(customer, file)

def read():
    global numberOfAccounts, customer
    try:
        with open(countOfAccounts, 'rb') as file:
            numberOfAccounts = pickle.load(file)

        with open(FILE_NAME, 'rb') as file:
            customer = pickle.load(file)
    except FileNotFoundError:
        pass

def main():
    read()
    while True:
        print("\nEnter your choice")
        print("1. Open Account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Display account")
        print("5. Delete account")
        print("6. Exit")

        choiceforbankaccount = int(input())
        if choiceforbankaccount == 1:
            openAccount()
        elif choiceforbankaccount == 2:
            depositMoney()
        elif choiceforbankaccount == 3:
            withdrawMoney()
        elif choiceforbankaccount == 4:
            printAccountInfo()
        elif choiceforbankaccount == 5:
            deleteAccount()
        elif choiceforbankaccount == 6:
            write()
            customerDetails()
            break
        else:
            print("Invalid choice !! Try again")

if __name__ == "__main__":
    main()
