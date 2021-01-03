

#https://github.com/JamariCJGoodridge/BasicBankApplication/blob/master/Python%20Saved%20Banking.py

#https://docs.python.org/3/library/logging.html#logging.LogRecord

#https://docs.python.org/3/library/datetime.html?highlight=hours%20minutes%20seconds


#START: Pyramid_Chain_Container1 WvvBank_Master_Ledger 20201205 ATMWvvBank/ATM
#Embed Code "Kryptheum PyramidChainContainer" Beta Virtual Machine"

#Virtual Universe, Registered Byte Particle Element", a universe, registered byte particle element, 
# that can never be directly detected, but whose existence does have measurable 
# "Store of unit value"(souv) effects. Quote: "Stephen Hawking's"


import math
import sys
import datetime
from datetime import date
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('Ledger.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

#logging.basicConfig(filename='Ledger.log', level=logging.INFO,
                    #format='%(asctime)s:%(levelname)s:%(message)s')


#formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

#file_handler.setLevel(logging.ERROR)

print("World Vision Virtual Bank Acctnum 5111948 Master LedgerBytes.\n")
print("When asked to make a Ledger/Transaction, you have several options to start.")
print("clear -> reseting all Ledger/Data.")
print("yes -> start of main loop.")
print("no -> end program.")
print("you can exit after any Ledger/Transaction by typing QUIT.\n")

def addStartingBalance():
    print("RESET STARTING LEDGER BALANCE?")
    addStart = str(input())
    addStart = addStart.lower()
    if addStart == "y" or addStart == "yes":
        file = open("Bank Data.txt", "w")
        file.write(str(100))
    print("RESET OLD LOGS?")
    erase = str(input())
    erase = erase.lower()
    if erase == "y" or erase == "yes":
        file = open("Transaction Log.txt", "w")
        file.write("START")
    prompt()

    

def prompt():
    print("Would you like to make a Ledger/Transaction?")
    transact = str(input())
    transact = transact.lower()
    startup(transact)

def startup(confirm):
    run = True
    while run:
      if confirm == "yes" or confirm == "y":
        transaction_option()
      elif confirm == "no" or confirm == "n" or confirm == "quit" or confirm == "q":
        print("Exiting...")
        sys.exit()
      elif confirm == "clear" or confirm == "c":
          addStartingBalance()
      else:
        print("Input invalid")
        prompt()

def transaction_option():
    print("\nWould you like to make a deposit or withdrawal")
    change = str(input(""))
    change = change.lower()
    if change == "deposit" or change == "d":
        deposit_money()
    elif change == "withdrawal" or change == "w":
        withdrawMoney()
    elif change == "quit" or change == "exit":
        print("Exiting Master Ledger...")
        sys.exit()
    else:
        print("Invalid input")
        
def checkBalance():
    file = open("Bank Data.txt", "r")
    print("Current balance")
    print(file.read())
    current = open("Bank Data.txt", "r").read()
    floatCurrent = float(current)
    file.close()
    
def deposit_money():
    checkBalance()
    depositAction()

def depositAction():
    try:
        file = open("Bank Data.txt", "r")
        current = open("Bank Data.txt", "r").read()
        floatCurrent = float(current)
        file.close()
    
        print("How much would you like to deposit?")
        addedAmount = input()
        floatAddedAmount = float(addedAmount)
        file = open("Bank Data.txt", "w")
        newAmount = floatCurrent + floatAddedAmount
        newAmount = str(newAmount)
        file.write(newAmount)
        file.close()
        file = open("Bank Data.txt", "r")
        print("New Amount is: ")
        print(file.read())
        file.close()
        transactionOccured = "+"
        transactionLogs(floatCurrent, transactionOccured, floatAddedAmount, newAmount)
    except ValueError:
        print("You provided an invalid input.")
    
    logger.info('Created Ledger: {} - {} - {} - {} - {} - {} - {}'.format(floatCurrent, transactionOccured, floatAddedAmount, newAmount, 'CurrentAcctBalance', 'TransactionAcctAmount', 'NewAcctBalance'))

def withdrawMoney():
    checkBalance()
    withdrawalAction()

def withdrawalAction():
    try:
        file = open("Bank Data.txt", "r")
        current = open("Bank Data.txt", "r").read()
        floatCurrent = float(current)
        file.close()
    
        print("How much would you like to withdraw?")
        addedAmount = input()
        floatAddedAmount = float(addedAmount)
        file = open("Bank Data.txt", "w")
        newAmount = floatCurrent - floatAddedAmount
        newAmount = str(newAmount)
        file.write(newAmount)
        file.close()
        file = open("Bank Data.txt", "r")
        print("New Amount is: ")
        print(file.read())
        file.close()
        transactionOccured = "-"
        transactionLogs(floatCurrent, transactionOccured, floatAddedAmount, newAmount)
    except ValueError:
        print("You provided an invalid input.")

 
    logger.info('Created Ledger: {} - {} - {} - {} - {} - {} - {}'.format(floatCurrent, transactionOccured, floatAddedAmount, newAmount, 'CurrentAcctBalance', 'AcctTransactionAmount', 'NewAcctBalance'))

    

def transactionLogs(floatCurrent, transactionOccured, floatAddedAmount,newAmount):
    LOG = open("Transaction Log.txt", "a")
    oldAmount = floatCurrent
    oldAmount = str(floatCurrent)
    transactionType = transactionOccured
    transactionAmount = floatAddedAmount
    transactionAmount = str(transactionAmount)
    updatedAmount = newAmount
    updatedAmount = str(newAmount)
    noww = datetime.today()
    LOG.write("\n\nOld AcctBalance: " + oldAmount)
    LOG.write("\nDepositTransaction Occured: " + transactionType + transactionAmount)
    LOG.write("\nNew AcctBalance: " + updatedAmount)
    LOG.write(noww.strftime('%c-%H-%M-%S.'))
    
#datetime_object = datetime.datetime.now()
#print(datetime_object)
    
def main():
    prompt()
    
main()



#https://docs.python.org/3/tutorial/datastructures.html?highlight=matrix%20arrays

# matrix = [
#       [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
#       [110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000],
#       [210000, 220000, 230000, 240000, 250000, 260000, 270000, 280000, 290000, 300000],
#       [310000, 320000, 330000, 340000, 350000, 360000, 370000, 380000, 390000, 400000],
#       [410000, 420000, 430000, 440000, 450000, 460000, 470000, 480000, 490000, 500000],
#       [510000, 520000, 530000, 540000, 550000, 560000, 570000, 580000, 590000, 600000],
#       [610000, 620000, 630000, 640000, 650000, 660000, 670000, 680000, 690000, 700000],
#       [710000, 720000, 730000, 740000, 750000, 760000, 770000, 780000, 790000, 800000],
#       [810000, 820000, 830000, 840000, 850000, 860000, 870000, 880000, 890000, 900000],
#       [910000, 920000, 930000, 940000, 950000, 960000, 970000, 980000, 990000, 1000000],
# ]

# print(matrix, c, 'Container1/1000000 BytesParticles', 'WorldVisionVirtualBank@mail.com')



