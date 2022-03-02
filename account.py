# everything inside a class must be indented

# capital A for a class
class Account:
    # will keep track of how many have been created
    numCreated = 0

    # constructor
    def __init__(self, initial):
        # self means you are using the reference of the specific account being accessed i.e. the right person's
        self.__balance = initial
        Account.numCreated += 1

    def deposit(self, amount):
        self.__balance += amount
        return

    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        return

    def getbalance(self):
        return self.__balance

    def __str__(self):
        return "I am a bank account. My balance is: " + str(self.getbalance())

    # allows us to add two bank accounts together by overriding the inherited add function
    def __add__(self, other):
        return self.getbalance() + other.getbalance()

# this isn't working check it
    # def main(self):
    #     homer = Account(350)
    #     print(homer.getbalance())
    #
    #
    # if __name__ == "__main__":
    #     main(self)