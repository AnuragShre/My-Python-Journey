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


def pay(bal,random_symbols):
    if random_symbols[0] == random_symbols[1] == random_symbols[2]:
        print("You won!")
        bal = 10
        return bal
    else:
        print("you lost!")
        bal = -10
        return bal


def spin(symbols,bal):


    random_symbols = []
    for i in range(3):
        random_symbols.append(random.choice(symbols))
        print(random_symbols[i],end=" | ")

    print("")
    return random_symbols


            

    

def main():
    bal= 0
   
    print("**********************************")
    print("* Welcome to Python Slot Machine *")
    print("**********************************")
    print("")
    print("We have following symbols")
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
    while bal > 0:
        random_symbols = spin(symbols,bal)
        print(bal)

        bal += pay(bal,random_symbols)
        print("Would you like to spin again?")
        ans = input("y/n: ")
        if ans != "y":
            break

if __name__ == "__main__":
    main()