# Main program for controlling a Bank made up of Accounts
  # Bring in all the code of the Bank class
from bank import *

# Create an instance of the Bank
oBank = Bank()

# Main code
# Create two test accounts
joesAccountNumber = oBank.createAccount('Joe', 111, '1')
print("Joe's account number is:", joesAccountNumber)

marysAccountNumber = oBank.createAccount('Mary', 222, '2')
print("Mary's account number is:", marysAccountNumber)

hikiAccountNumber = oBank.createAccount('Hiki', 333, '3')
print("Hiki's account number is:", hikiAccountNumber)

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w ')
    print()
    
    action = input('What do you want to do? ') 
    action = action.lower()
    action = action[0] # grab the first letter 
    print()
    
    if action == 'b': 
        oBank.balance()
        
    elif action == 'c': 
        oBank.closeAccount()
        
    elif action == 'd':
          oBank.deposit()
          
    elif action == 'o':
        oBank.openAccount()
        
    elif action == 's':
        oBank.show()
        
    elif action == 'q':
        break
    elif action == 'w':
        oBank.withdraw()
        
    else:
        print('Sorry, that was not a valid action. Please try again.')

print('Done')
