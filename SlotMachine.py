import random



def Deposit(bal):
    check = True

    while check:
        depo = input("Enter the amount you would like to deposit: ")
        if depo.isdigit:
            bal += int(depo)
            check = False
            return bal
        else:
            print("Please enter a valid amount")



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

    print(f"Your current balence: {bal}")




if __name__ == "__main__":
    main()