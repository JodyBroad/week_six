from account import Account

lisa_account = Account(1000)
lisa_account.deposit(200)
print("Lisa's balance is: ", lisa_account.getbalance())

bart_account = Account(50)
print("Bart's balance is: ", bart_account.getbalance())

lisa_account.withdraw(75)
bart_account.deposit(75)

print("Lisa's balance is: ", lisa_account.getbalance())
print("Bart's balance is: ", bart_account.getbalance())

# will not give useful information, will tell you the type of account and memory value essentially, without a function
# in the class
print(lisa_account)
print(bart_account)

# print stringifies every parameter we pass to it

total_balance = lisa_account.getbalance() + bart_account.getbalance()
print(total_balance)

total_balance2 = lisa_account + bart_account
print(total_balance2)
