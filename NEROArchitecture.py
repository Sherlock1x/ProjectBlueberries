
# NERO Architecture Start "Q"Nero-Whale", "Patch 101 for the Dollar"

#https://github.com/JamariCJGoodridge/BasicBankApplication/blob/master/Python%20Saved%20Banking.py

#https://docs.python.org/3/library/logging.html#logging.LogRecord

#https://docs.python.org/3/library/datetime.html?highlight=hours%20minutes%20seconds


#START: Pyramid_Chain_Container1 WvvBank_Master_Ledger 20201205 ATMWvvBank/ATM
#Embed Code "Kryptheum PyramidChainContainer" Beta Virtual Machine"

#Accretion/Inheritance Adromeda Galaxy , M31, Matrix Invenit Well

#Virtual Universe, Registered Byte Particle Element", a universe, registered byte particle element, 
# that can never be directly detected, but whose existence does have measurable 
# "Store of unit value"(souv) effects. Quote: "Stephen Hawking's"

#Automatic Finance with Pythonmain.py All Withdrawal/DepositTransactions MTD/YTD 

#q_Nero_Architecture_open_source_AI Gold/Silver Collateral Multiplier.....

#BankData.txt
#mala.txt
#NEROLedger.log
#TransactionLog.txt

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
from rich.console import Console
from PIL import Image
#z=1/3
#s=666245

console = Console()


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

print("[bold][blue] World Vision Virtual Bank Acctnum 5111948 Master LedgerBytes.\n[/blue]")
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
        print("[bold][blue] Exiting Master Ledger 'Q' Nero Thanks for Banking with Us... [/blue]")
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
    LOG.write("\nWithdrawalTransaction Occured: " + transactionType + transactionAmount + transactionAmount)   #Updated 8-13-2025
    LOG.write("\nNew AcctBalance: + 32621.81 oz/GLD Collateral = Basex New ACCTBalance $" + updatedAmount)
    LOG.write("\nNew AcctBalance: "" Basex Accretion/Inheritance " + updatedAmount)
    LOG.write(noww.strftime('%c-%H-%M-%S.'))
    LOG.write("[red] \nNew Cumalative AcctPayableAmountCurrentXPense, $20981.00 +32621.81 oz/GLD Collateral = Pyramidzxy New ACCTBalance $$120700710 [/red]")
    logger.info("[bold][red] \nNew Cumalative AcctPayableAmountCurrentXPense, $20981.00 balance + 32621.81 oz/GLD Collateral = New Basex ACCTBalance $120700710 [/red]")

    #Economic Measurements transactionLogs
    
    h=(30175177/3700,"",'h Gold in ozs = Economic Measurement Apexy SVAlue Current Balance Collayeral YTD')
    print()
    b=(120700710/3700,"",'b Gold in ozs = Economic Measurement WellMx Pyramidzxy $$Value Current Balance Collateral YTD')
    print()
    c=(241401420/6400,"",'c Gold in ozs = Economic Measurement Pyramidzxy $$Value Future Value Current Balance Collateral YTD')
    print()
    #y=(84682042-1880,"", 'Economic Measurement Pyramidzxy $$Value Current Balance YTD')
    print()
    w=(1/3*90525533+90525533,"",'w Economic Measurement WellMx Pyramidxxy Chain Basex/Apexy Derivative')  #Measurement Pyramid Chain Base Derivative
    print()   
    oz=(90525533/3700.00,"",'oz Gold in ozs= WellMx Basex $Value Current Balance Collateral')   #Quantum Entanglement Particles Higgs Boson Field Electrons 
    print()
    wts=(90525533/3700.00*10,"",'wts Silver in ozs= Basex $Value Current Balance Collateral')  
    print()                                                                     # +- measurement  | Gold in oz's = $ Value, Gold.com
    r=requests.head('https://www.gold.com/get')
    print(r.url)                                                                    

    ww=(1/3*1000000+1000000*1000,"",'ww Parch 101 for the Dollar,"",Test Function Only')
    print()
    q=(1/3*90525533+90525533-90525533,"",'q Apexy WellMx Pyrimid Derivative')
    print()
    #wz=(1987631-1490723,'Delta Derivative Appex Pyramid')   #Delta Derivative Appex Pyramid
    print()
    wt=(90525533-0,"",'wt WellMx Basex Withdrawel Cumalative AcctPayable New current Balance$$ MTD')  #Cumalative AcctPayable Xpense current Balance$$
    print()
    wtt=(1880+19101,"",'wtt WellMx Cumalative AcctPayable Xpense$$ YTD')    #Cumalative AcctPayable Xpense $$ #"Chapter6-3py", Updating Ledger Log...
    print()
    fv=(120700710*2,"",'fv Economic Measurement Future $$Value Pyramidzxy Accretion and Inheritance')
    print()
    d=(63525533+27000000,"","[bold green]d WellMx Deposit AcctRec[/green]")
    print()
    j=(90525533+30175177,"","[bold yellow]j WellMx Pyramidzxy AcctPay Apexy and Basex[/yellow]")

    print(h,b,c,w,oz,ww,q,wt,wtt,wts,fv,d,j)

    numbers = arr.array('i', [86000000,87000000,88000000,89000000,90525533])  #Basex


    print(numbers[-1])    # https://www.freecodecamp.org/news/python-slicing-how-to-slice-an-array/
    c = input("PLease enter your name:")
    
    print('[bold][red] Future Value Wedge Collateral Andromeda Galaxy FailSafe [/red]')
    print(...)
    print('[bold][green] When a black hole feeds on stars, gas or dust the meal produces jets of GOLD Particles and radiation blasting out [/green]')
    print(...) 
    print('[green] from the black holes poles at near light speed [/green]')
    print(...) 
    print('[green] They can extend for thousand of light years into space. Yield 90525533 oz / $3700.00/ gold = PV $90.5 mil ,FV X.0bln. [/green]')
    print(...)


    print('[bold[yellow] worldvisionvirtualbank1@gmail.com [/yellow]')
    print(...)

    print('[bold][yellow] Registered Memory Creation GoldByte Particle Element $84700710.0 = 3700 oz/GoldByte Particle Element [/yellow]')
    print(...) 
    print('[bold[yellow] as collateral..Virtual Universe | from M31 Andromeda galaxy [/yellow]')
    print(...) 
    print('[bold][yellow] Light from this galaxy took 2.65 million light years to reach the camera sensor that took this picture. [/yellow]')

    #https://www.youtube.com/watch?v=DKPRDCAOnXM


balance = 20981.0    #Total Cumalative AcctPayableAmount Current Balance XPense YTD
while True:
    try:
        num = float(input('XPense:'))
        break
    except ValueError:
        print('Must be a valid quantity.')

balance += num
print(f'Balance:(balance)')

print(balance,"", "[bold red] Total Cumalative AcctPayableAmount Current Balance XPense")

logger.error("[bold red] \nNew Cumalative AcctAmount Current XPense, $20981.00 balance += num [/red]")  #Output  Current Xpense $$$
  
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
print(primes,"","[bold][green] Memory Registration/Title/Transaction[/green]")  

for i in tqdm(range(0, 100), desc="Text Processing Matrix 10x10 Shape"):    #Progress Bar tqdm
    sleep(0.1)

elems  = ['A YTD Basex AcctBal', 'B YTD Gold ozs', 'C YTD AcctPay','D YTD Apexy', 'E YTD Pyramidzxy Chain']
numbers = [90525533, 24466.36, 20981, 30175177, 120700710]   #New AcctBalance $$ Matrix 10x10 Shape line 312

zipped = zip(numbers, elems)

console.print("([bold yellow] '90525533 A YTD Basex AcctBal' "", '24466.36 B YTD Gold ozs' "", '20981 C YTD AcctPay' "", '30175177 D YTD Apexy' "", '120700710 E YTD Pyramidzxy Chain')")
console.print()

print(list(zipped))

i = 1
while i < 6:
    print(i)
    i += 1

url=("https://github.com/Sherlock1x/ProjectBlueberries/blob/master/newplot%20-%20Copy.PNG")
X=url
show=(X)

url=("https://github.com/Sherlock1x/ProjectBlueberries/blob/master/newplotSept25.png")
x=url
show=(X)

url=("https://github.com/Sherlock1x/ProjectBlueberries/blob/master/newplot2.png")
X=url
show=(X)

url=("https://github.com/Sherlock1x/ProjectBlueberries/blob/master/sample_bank1_statement.csv.xlsx%20%20-%20%20version%201.0.%204.20.2025%205.05%20PM.csv")
x=url
show=(X)

url=("https://github.com/Sherlock1x/ProjectBlueberries/blob/master/triangle-shapes.gif")
x=url
show=(X)

url = ("https://github.com/Sherlock1x/ProjectBlueberries/blob/master/!!!!!!!!!!!!!!!AndromedaGalaxy1.gif")
x=url
show=(X)


# Read the image

im = Image.open("C:\\Users\\Spect\\OneDrive\\VSCode-overview\\Blueberries\\PyramidChain.jpg")

im_rotate = im.rotate(0)

im_rotate.show()

im = Image.open("C:\\Users\\Spect\\OneDrive\\VSCode-overview\\Blueberries\\!!!!!!!!!!!!!!!AndromedaGalaxy1.gif")
im_rotate = im.rotate(360)
im_rotate.show()


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
#       [110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000],  # $63,525,533.00 Basex  col2/row6
#       [210000, 220000, 230000, 240000, 250000, 260000, 270000, 280000, 290000, 300000],  # $$84,679,535.00  Pyramidzxy
#       [310000, 320000, 330000, 340000, 350000, 360000, 370000, 380000, 390000, 400000],  # The Invenite Well
#       [410000, 420000, 430000, 440000, 450000, 460000, 470000, 480000, 490000, 500000],  # Economic measurement = New AcctBalance
#       [510000, 520000, 530000, 540000, 550000, 560000, 570000, 580000, 590000, 600000],  # 22886.36oz GoldBytesParticles
#       [610000, 620000, *630000, 640000, 650000, 660000, 670000, 680000, 690000, 700000],  #https://www.youtube.com/watch?v=xWb97DEq864
#       [710000, 720000, 730000, 740000, 750000, 760000, 770000, 780000, 790000, 800000],
#       [810000, 820000, 830000, 840000, 850000, 860000, 870000, 880000, 890000, 900000],    # 228863.60 oz Silver see above info
#       [910000, 920000, 930000, 940000, 950000, 960000, 970000, 980000, 990000, 1000000],
# ]

# print(matrix, c, 'Container1/1000000 GoldBytesParticles', 'WorldVisionVirtualBank1@gmail.com')

#Pyramidzxy Chain = Basex + Apexy
#"V=1/3bh", where b is the area of the base and h the height from the basex to the apexy. 

#DISCLAIMER: This e-mail and any file(s) transmitted with it, is intended for the exclusive use by the person(s) mentioned 
#above as recipient(s). This e-mail may contain confidential information and/or information protected by intellectual property 
#rights or other rights. If you are not the intended recipient of this e-mail, you are hereby notified that any dissemination, 
#distribution, copying, or action taken in relation to the contents of and attachments to this e-mail is strictly prohibited and  
#may be unlawful. If you have received this e-mail in error, please notify the sender and delete the original and any copies of 
#this e-mail and any printouts immediately from your system and destroy all copies of it. 


















