
#Python Loops Tutorial | Python For Loop | While Loop Python | Python Training | Edureka

#https://www.youtube.com/watch?v=zFvoXxeoosI

print('Welcome to WvvBank ATM WorldVisionVirtualBank@mail.com')
restart = ('Y')
chances = 3
balance = 1000000 
while chances>  0:
    pin = int(input('Please enter 7 Digit Pin: ')) 
    if pin == (5111948):
        print('You entered your pin correctly\n')
        while restart not in ('n', 'No', 'no', 'N'):
            print('Please Press 1 For Your MatrixBalance\n')
            print('Please Press 2 To Make Withdrawel\n')
            print('Please Press 3 To Make Payment in\n')
            print('Please Press 4 To Return Card\n')
            option = int(input('What Would Like to choose?'))
            if option == 1:
                print('Your Balance is Bytes',balance,'/n')
                restart = input('Would You Like to go Back?')
                if restart in ('n', 'No', 'no', 'N'):
                    print('Thank You')
                    break
            elif option == 2:
                
                option2 = ('y')
                withdrawel = float(input('How Much Would You Like To Withdrawel? \n $10/$20/$30/$40/$50/$100/$500/$1000/$10000'))
                if withdrawel in [10, 20, 30, 40, 50, 100, 500, 1000, 10000]:
                    balance = balance - withdrawel
                    print('\nYour Balance is now Bytes',balance)
                    restart = input('Would you like to go back? ')
                    if restart in('n', 'No', 'no', 'N'):
                        print('Thank You')
                        break
                elif withdrawel != [10, 20, 30, 40, 50, 100, 500, 1000, 10000]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawel == 1:
                    withdrawel = float(input('Please Enter Desire Amount:'))

            elif option == 3:
                Pay_in = float(input('How Much Would You Like to Pay in?'))
                balance = balance + Pay_in
                print('\n Your Balance is now Bytes',balance)
                restart = input('Would You Like To Go Back?')
                if restart in('n', 'No', 'no', 'N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait while your card is Returned...\n')
                print('Thank you for your service')
                break
            else:
                print('Please Enter Correct Number. \n')
                restart = ('y')
    elif pin != ('5111948'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break



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


                

                    
                    







