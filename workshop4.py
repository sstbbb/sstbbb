class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self, balance):
        self.balance = balance

    def withdraw(self, balance):
        self.balance -= balance

    def deposit(self, balance):
        self.balance += balance

    def transfer(self, balance):
        self.balance -= balance

    def request(self, balance):
        self.balance += balance


bankuser2 = BankUser("Fred", 2222, "denver")
bankuser1 = BankUser("Sean", 4321, "colorado")
bankuser2.deposit(5000)
password = ''

print(bankuser2.name, "has a balance of: $" + str(bankuser2.balance))
print(bankuser1.name, "has a balance of: $" + str(bankuser1.balance))
print(bankuser2.name, "is tranferring $" + str(500), "to", bankuser1.name)
print("Authentication required")
pin = input("Enter your pin: ")
if pin == "2222":
    print("Transfer authorized")
    print("Transfering $" + str(500), "to", bankuser1.name)
    bankuser2.transfer(500)
    bankuser1.deposit(500)
    print(bankuser2.name, "has a balance of: $", str(bankuser2.balance))
    print(bankuser1.name, "has a balance of: $", str(bankuser1.balance))
else:
    print("Invalid PIN. Transaction cancelled")
    print(bankuser2.name, "has a balance of: $", str(bankuser2.balance))
    print(bankuser1.name, "has a balance of: $", str(bankuser1.balance))

print("")
print("You are requesting $" + str(250), "from", bankuser2.name)
print("User authentication is required...")
pin = input("Enter Fred's pin: ")
if pin != "2222":
    print("Invalid pin")
    print(bankuser2.name, "has a balance of: $", str(bankuser2.balance))
    print(bankuser1.name, "has a balance of: $", str(bankuser1.balance))
elif pin == "2222":
    password = input("Enter your password ")
    if password != "denver":
        print("Wrong password")
        print(bankuser2.name, "has a balance of: $", str(bankuser2.balance))
        print(bankuser1.name, "has a balance of: $", str(bankuser1.balance))
    elif password == "denver":
        print("Request authorized")
        print("Fred sent $" + str(250))
        bankuser2.transfer(250)
        bankuser1.request(250)
        print(bankuser2.name, "has a balance of: $", str(bankuser2.balance))
        print(bankuser1.name, "has a balance of: $", str(bankuser1.balance))
    else:
        print("")

    # Driver Code for Task 1

    # user1 = User("Bob", 1234, "password")
    # print(user1.name, user1.pin, user1.password)

    # Driver code for Task 2
    # user1 = User("Bob", 1234, "password")
    # print(user1.name, user1.pin, user1.password)
    # user1.change_name("Sean")
    # user1.change_pin(4321)
    # user1.change_password("colorado")
    # print(user1.name, user1.pin, user1.password)

    # Driver code for task 3

    # bankuser1 = BankUser("Sean", 4321, "colorado")
    # print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)

 # Driver code for task 4

 # bankuser1 = BankUser("Sean", 4321, "colorado")
    # print("Sean has a balance of:", bankuser1.balance)
    # bankuser1.deposit(1000)
    # print("Sean has a balance of:", bankuser1.balance)
    # bankuser1.withdraw(500)
 # print("Sean has a balance of:", bankuser1.balance)
 # bankuser1.deposit(1000)
 # print("Sean has a balance of:", bankuser1.balance)

 # Driver code for task 5

 # bankuser2.withdraw(value)
 # bankuser1.deposit(value)
 # print("Fred has a balance of:", bankuser2.balance)
 # print("Sean has a balance of:", bankuser1.balance)
