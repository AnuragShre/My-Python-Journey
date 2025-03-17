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

def spin(symbols):
    random_symbols = []
    for i in range(3):
        random_symbols.append(random.choice(symbols))

    

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

    
    spin(symbols)




if __name__ == "__main__":
    main()