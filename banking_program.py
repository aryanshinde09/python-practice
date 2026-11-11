balance = 100
deposit = 0
withdraw = 0

try:
    while True:
        print("For Deposit press 1 / For Withdraw press 2 / For show-balance press 3/ press 0 to quit")
        user = int(input("What you wanna do?: "))
        print("-----------------------------------------------------------------")

        # Deposit logic 
        if user == 1:
            deposit = int(input("how much money to deposit:"))
            if deposit <= 0:
                print("Not a valid amount to deposit")
            else:
                balance += deposit
                print("deposited Successfully!")
            print("-----------------------------------------------------------------")

        # Withdraw logic 
        if user == 2:
            withdraw = int(input("how much money to withdraw:"))
            if withdraw <= 0:
                print("Not a valid amount to withdraw")
            if withdraw > balance:
                print("you dont have enough money to Withdraw son !")
            else:
                balance -= withdraw
            
            print("-----------------------------------------------------------------")

        #balance logic
        if user == 3:
            print(f'You have {balance} in you account')
            print("-----------------------------------------------------------------")

        #Quitting the loop/banking program
        if user == 0:
            break
except:
    print("Enter a valid number")

