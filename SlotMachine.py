import random



def Deposit(bal):
    check = True

    while check:
        depo = input("Enter the amount you would like to deposit: ")
        if not depo.isdigit():
             print("Please enter a valid amount")
             continue
        else:
            check = False
    bal += int(depo)
    return bal



def main():
    bal= 0
   
    print("**********************************")
    print("* Welcome to Python Slot Machine *")
    print("**********************************")
    print("")
    print("The following symbols are available")
    print("")
    symbols = ["🍉","🍌","🔔","🌟"]
    i = 0

    print("***********************")
    while i<=3:
        print(symbols[i],end=" | ")

        i+=1
    print("")
    print("***********************")
    
    bal = Deposit(bal)

    print(f"Your current balance: {bal}")




if __name__ == "__main__":
    main()