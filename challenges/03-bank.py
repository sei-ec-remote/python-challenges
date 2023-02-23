
def the_bank():
    print("\nHey there! Welcome to Carl's Money Place! \n")
    finished = 'no'
    balance = 0
    while finished == 'no':
        transaction=input("\nWhat're you lookin' to do? (deposit, withdraw, check_balance)\n \n")
        if transaction == "deposit":
            amount=int(input("\nHow much money you like to put in the place?\n \n"))
            balance=balance+amount
            print(f"\nYou have successfully put {amount} in the place\n")
        if transaction == "withdraw":
            amount=int(input("\nHow much money you like to take from the place?\n \n"))
            if amount > balance:
                print(f"\nYou don't have that much money in the place! This ain't a charity! You only have {balance}.\n")
            else:
                balance=balance-amount
                print(f"\nYou have successfully taken {amount} from the place\n")
        if transaction == "check_balance":
            print(f"\nYou currently have {balance} in the place\n")
        finished=input("\nAre you finished at the place? (yes/no)\n \n")
    print("\nHope to see you again at the place sometime soon!")

the_bank()