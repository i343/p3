# Non-OOP Bank
# Version 5
# Any number of accounts - with a list of dictionaries

accountsList = [] 

def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = {'name':aName, 'balance':aBalance, 'password':aPassword}
    accountsList.append(newAccountDict)
    
def show(accountNumber):
    global accountsList
    print('Account', accountNumber) 
    thisAccountDict = accountsList[accountNumber]
    print('Name', thisAccountDict['name'])
    print('Balance:', thisAccountDict['balance'])
    print('Password:', thisAccountDict['password'])
    print()

def getBalance(accountNumber, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    return thisAccountDict['balance']

def deposit(amountToDeposit, password): 
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
    if password != accountPassword:
        print('Incorrect password')
        return None
    accountBalance = accountBalance + amountToDeposit
    return accountBalance

def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != accountPassword:
        print('Incorrect password for this account')
        return None

    if amountToWithdraw > accountBalance:
        print('You cannot withdraw more than you have in your account')
        return None
    accountBalance = accountBalance - amountToWithdraw
    return accountBalance

# Create two sample accounts
print("Joe's account is account number:", len(accountsList))

newAccount("Joe", 100, 'soup')
print("Mary's account is account number:", len(accountsList))
newAccount("Mary", 12345, 'nuts')

print(accountsList)

# while True:
#     print()
#     print('Press b to get the balance')
#     print('Press d to make a deposit')
#     print('Press n to create a new account')
#     print('Press w to make a withdrawal')
#     print('Press s to show all accounts')
#     print('Press q to quit')
#     print()
#     action = input('What do you want to do? ')
#     action = action.lower() # force lowercase
#     action = action[0] # just use first letter

#     print()
#     if action == 'b':
#         print('Get Balance:')
#         userAccountNumber = input('Please enter your account number: ')
#         userAccountNumber = int(userAccountNumber)
#         userPassword = input('Please enter the password: ')
#         theBalance = getBalance(userAccountNumber, userPassword)

#         if theBalance is not None:
#             print('Your balance is:', theBalance)
#         elif action == 'd':
#             print('Deposit:')

#         userAccountNumber= input('Please enter the account number: ')
#         userAccountNumber = int(userAccountNumber)
#         userDepositAmount = input('Please enter amount to deposit: ')
#         userDepositAmount = int(userDepositAmount)
#         userPassword = input('Please enter the password: ')
#         newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
#         if newBalance is not None:
#             print('Your new balance is:', newBalance)
#     elif action == 'n':
#         print('New Account:')
#         userName = input('What is your name? ')
#         userStartingAmount = input('What is the amount of your initial deposit? ')
#         userStartingAmount = int(userStartingAmount)
#         userPassword = input('What password would you like to use for this account? ')
#         userAccountNumber = len(accountsList)
#         newAccount(userName, userStartingAmount, userPassword)
#         print('Your new account number is:', userAccountNumber)
#     else:
#         print()
    
print('Done')

# --- snipped additional user interface ---
