import random


def main():
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




if __name__ == "__main__":
    main()