
#NERO Architecture Start "Nero-Whale"

#https://github.com/JamariCJGoodridge/BasicBankApplication/blob/master/Python%20Saved%20Banking.py

#https://docs.python.org/3/library/logging.html#logging.LogRecord

#https://docs.python.org/3/library/datetime.html?highlight=hours%20minutes%20seconds


#START: Pyramid_Chain_Container1 WvvBank_Master_Ledger 20201205 ATMWvvBank/ATM
#Embed Code "Kryptheum PyramidChainContainer" Beta Virtual Machine"

#Virtual Universe, Registered Byte Particle Element", a universe, registered byte particle element, 
# that can never be directly detected, but whose existence does have measurable 
# "Store of unit value"(souv) effects. Quote: "Stephen Hawking's"

import rich
import math
import sys
import datetime
from datetime import date
from datetime import datetime
import logging
from rich.logging import RichHandler
from rich import print
from tqdm import tqdm 
from time import sleep
import requests
import array as arr 
#z=1/3
#s=666245

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('NEROLedger.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

logging.basicConfig(filename="Kamala.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

#logging.basicConfig(filename='Ledger.log', level=logging.INFO,
                    #format='%(asctime)s:%(levelname)s:%(message)s')


#formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

#file_handler.setLevel(logging.ERROR)

print("[blue] World Vision Virtual Bank Acctnum 5111948 Master LedgerBytes.\n[/blue]")
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
    startup(transact)                             #startup(transact)

def startup(confirm):  
    run = True
    while run:
      if confirm == "yes" or confirm == "y":
        transaction_option()                               #transaction_option()
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
        withdrawMoney()                                        #withdrawMoney()
    elif change == "quit" or change == "exit":
        print("[blue] Exiting Master Ledger Nero Thanks for Banking with Us... [/blue]")
        sys.exit()
    else:
        print("Invalid input")
        
def checkBalance():
    file = open("Bank Data.txt", "r")                     #file = open("Bank Data.txt", "r")
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
    checkBalance()                                 #checkBalance()
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

    

def transactionLogs(floatCurrent, transactionOccured, floatAddedAmount, newAmount):
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
    LOG.write("\nWithdrawalTransaction Occured: " + transactionType + transactionAmount)
    LOG.write("\nNew AcctBalance: + 12613.26oz/GLD Collateral = New ACCTBalance $" + updatedAmount)
    LOG.write("\nNew AcctBalance: " + updatedAmount)
    LOG.write(noww.strftime('%c-%H-%M-%S.'))
    LOG.write("[red] \nNew Cumalative AcctPayableAmountCurrentXPense, $11438.00 + 12613.26oz/GLD Collateral = New ACCTBalance $ [/red]")
    logger.info("[red] \nNew Cumalative AcctPayableAmountCurrentXPense, $11438.00 balance + 12613.26oz/GLD Collateral = New ACCTBalance $ [/red]")
    
    h=1
    b=1
    y=1000
    w=(1/3*42885076+42885076,"",'Measurement Pyramid Chain Basex/Apexy Derivative')  #Measurement Pyramid Chain Base Derivative
    oz=(42885076/3400.00,"",'Gold in ozs=$Value Current Balance Collateral')   #Quantum Entanglement Particles Higgs Boson Field Electrons 
    wts=(42885076/3400.00*10,"",'Silver in ozs=$Value Current Balance Collateral')                                                                       # +- measurement  | Gold in oz's = $ Value, Gold.com
    r=requests.head('https://www.gold.com/get')
    print(r.url)                                                                    

    ww=(1/3*1000000+1000000,"",'Test Function Only')
    q=(1/3*42885076+42885076-42885076,"",'Apexy Pyrimid Derivative')
    #wz=(1987631-1490723,'Delta Derivative Appex Pyramid')   #Delta Derivative Appex Pyramid
    wt=(42888655-3579,"",'Cumalative AcctPayable New current Balance$$')  #Cumalative AcctPayable Xpense current Balance$$
    wtt=(3579+7859,"",'Cumalative AcctPayable Xpense$$')    #Cumalative AcctPayable Xpense $$ #"Chapter6-3py", Updating Ledger Log...

    print(h,b,w,oz,ww,q,wt,wtt,wts)

    numbers = arr.array('i', [440000,450000,460000,470000,42885076])


    print(numbers[-1])    # https://www.freecodecamp.org/news/python-slicing-how-to-slice-an-array/
    c = input("PLease enter your name:")
    
    print('[red] Future Value Wedge Collateral MilkWays FailSafe [/red]')
    print(...)
    print('[green] When a black hole feeds on stars, gas or dust the meal produces jets of GOLD Particles and radiation blasting out [/green]')
    print(...) 
    print('[green] from the black holes poles at near light speed [/green]')
    print(...) 
    print('[green] They can extend for thousand of light years into space. Yield 16000 oz x $3400.00/ gold = PV $54.4Mmil ,FV54.4bln. [/green]')
    print(...)


    print('[blue] worldvisionvirtualbank1@gmail.com [/blue]')
    print(...)

    print('[green] Registered Memory Creation GoldByte Particle Element $1,4855076.00 = 3400 oz/GoldByte Particle Element [/green]')
    print(...) 
    print('[green] as collateral..Virtual Universe | from M31 Andromeda galaxy [/green]')
    print(...) 
    print('[green] Light from this galaxy took 2.65 million light years to reach the camera sensor that took this picture. [/green]')

    #https://www.youtube.com/watch?v=DKPRDCAOnXM


balance = 11438.0    #Total Cumalative AcctPayableAmount Current Balance XPense YTD
while True:
    try:
        num = float(input('XPense:'))
        break
    except ValueError:
        print('Must be a valid quantity.')

balance += num
print(f'Balance:(balance)')

print(balance,"", "[red] Total Cumalative AcctPayableAmount Current Balance XPense[/red]")

logger.error("[red] \nNew Cumalative AcctAmount Current XPense, $11438.00 balance += num [/red]")  #Output  Current Xpense $$$
  
nums = list(range (1, 100))

def is_prime(n):
    if n <2:
        return False
    
    if n ==2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

primes = filter(is_prime, nums)   #add list before filter
print(primes,"","[green] memory registration/Title[/green]")  

for i in tqdm(range(0, 100), desc="Text Processing Matrix 10x10 Shape"):    #Progress Bar tqdm
    sleep(0.1)

elems  = ['A', 'B', 'C','D']
numbers = [42885076, 2, 3, 4]   #New AcctBalance $$ Matrix 10x10 Shape line 312

zipped = zip(numbers, elems)

print(list(zipped))

i = 1
while i < 6:
    print(i)
    i += 1

#def transactionLogs(floatCurrent, transactionOccured, floatAddedAmount, newAmount):
    #LOG = open("Transaction Log.txt", "a")
    #LOG.write(f'Balance:(balance)',(balance))


    #print("Cumalative Account Amount")

    #print(10699.00)
    
#datetime_object = datetime.datetime.now()
#print(datetime_object)
    
def main(): 
    prompt()                   #promp()
    
main()                         #main()

#if__name__ = '__main__'
#main()



#print('[red]Quantum Entanglement Teleportation from Andromeda Galaxy M31 Matrix 10x10 Shape 2.65mly away[/red]')

#https://docs.python.org/3/tutorial/datastructures.html?highlight=matrix%20arrays

# matrix = [
#       [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
#       [110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000],  # $1,488,655.00  col8/row5
#       [210000, 220000, 230000, 240000, 250000, 260000, 270000, 280000, 290000, 300000],
#       [310000, 320000, 330000, 340000, 350000, 360000, 370000, 380000, 390000, 400000],  # The Invenite Well
#       [410000, 420000, 430000, 440000, 450000, 460000, 470000, 480000, 490000, 500000],  # measurement = New AcctBalance
#       [510000, 520000, 530000, 540000, 550000, 560000, 570000, 580000, 590000, 600000],  # 437.84 oz GoldBytesParticles
#       [610000, 620000, 630000, 640000, 650000, 660000, 670000, 680000, 690000, 700000],  #https://www.youtube.com/watch?v=xWb97DEq864
#       [710000, 720000, 730000, 740000, 750000, 760000, 770000, 780000, 790000, 800000],
#       [810000, 820000, 830000, 840000, 850000, 860000, 870000, 880000, 890000, 900000],    # 4378.4 oz Silver see above info
#       [910000, 920000, 930000, 940000, 950000, 960000, 970000, 980000, 990000, 1000000],
# ]

# print(matrix, c, 'Container1/1000000 GoldBytesParticles', 'WorldVisionVirtualBank1@gmail.com')












