print("Welcome to ICICI Bank ATM")
restart = ('Y')
chances = 3
balance = 2000
while chances >= 0:
    pin = int(input('Please Enter 4 digit pin\n'))
    if pin == (1234):
        print('success!\n')
        while restart not in ('n', 'NO', 'no', 'N'):
            print('Please press\n 1 for check balance\n 2 for Withdrawal\n 3 for pay in\n 4 to Return Card')
            option = int(input('Enter:'))
            if option == 1:
                print('Your Balance is Rs', balance, '\n')
                restart = input('Would you like to go back?')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawal = float(input('How much would you like to withdraw? \n Rs100/Rs200/Rs500/Rs1000/Rs2000/Rs5000\n'))
                if withdrawal in [100, 200, 500, 1000, 2000, 5000]:
                    balance = balance - withdrawal
                    print('\nYour balance is now RS', balance)
                    restart = input('Would you like to go back?')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank You')
                        break
                elif withdrawal != [100, 200, 500, 1000, 2000, 5000]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawal == 1:
                    withdrawal = float(input('Please Enter Desired amount:'))

            elif option == 3:
                Pay_in = float(input('How much would you like to Pay In'))
                balance = balance + Pay_in
                print('\nYour Balance is now Rs', balance)
                restart = input('Would you like to go back?')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait while your card is returned...\n')
                print('Thank you for your service')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\n No more tries')
            break
