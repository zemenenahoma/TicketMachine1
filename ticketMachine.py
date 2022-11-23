import time

print("Welcome to our products!")
def cosmotic():
    cosId1="C"
    tmstart=54
    timeTowait=3
    while True:
        print("Your ticket Id is ", cosId1, "-", tmstart, "Please wait and someone will assist you  in", timeTowait,"minutes")
        neUser = input(f"Enter  {cosId1} to get next Id if you want or enter n to finish and to take your ticket  : ")
        if neUser == "n":
            exit(0)
        tmstart = tmstart + 1
    return 0
def perfume():
    perId1 = "P"
    timeTowait=3
    tmstart = 54
    print("Your ticket Id is ", perId1, "-", tmstart, "Please wait and someone will assist you  in", timeTowait,"minutes")
    while True:
        neUser = input(f"Enter  {perId1} to get next Id if you want or enter n to finish and to take your ticket  : ")
        if neUser == "n":
                exit(0)
        tmstart = tmstart + 1
        print("Your ticket Id is", perId1, "-", tmstart, "Please wait and someone will assist you  in",timeTowait, "minutes")
    return 0


def medicen():
    medId1 = "M"
    tmstart = 54
    timeTowait=3

    print("Your ticket Id is", medId1, "-", tmstart, "Please wait and someone will assist you  in", timeTowait,"minutes")
    while True:
        neUser=input(f"Enter  {medId1} to get next Id if you want or enter n to finish and to take your ticket  : ")
        if neUser=="n":
            exit(0)
        print(medId1,"-",tmstart,"Here you are your ticket Id")
        tmstart=tmstart+1
        print("Your ticket Id is",medId1,"-",tmstart,"Please wait and someone will assist you  in",timeTowait,"minutes")
    return 0

list = ['34563545', '873645545']
count = 0
limit = 3
while count < limit:
    id = input("Enter id")


        # print(count)
    if id in list and count < limit:
        def main():
            print("""
                     Press 1 for  cosmotics
                     Press 2 for perfume
                     Press 3 for medicen 
                     """)
            option = int(input("please choose the area you want to buy a products and to take ticket."))
            if option == 1:
                print("You have choosed to ticket of cosmotic")
                cosmotic()
            elif option == 2:
                print("You have choosed to ticket of perfume")
                perfume()
            elif option == 3:
                print("You have choosed to ticket of medicen")
                medicen()
        main()


    else:
        print("Try again!")
        count += 1

else:
    print("You have been blocked!,Try again after ",3,"minutes")
    Time = int(input("please enter finshed time: "))
    for T in range(0,Time):
        time.sleep(1)
        print(f"00:00:0{T}")