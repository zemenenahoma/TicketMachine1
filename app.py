import time
from utility1 import cosmotic
from utlity2 import perfume
from utlity3 import medicen
def maintomain():
    list = ['34563545', '873645545']
    count = 0
    limit = 3
    while count < limit:
        id = input("Enter id")


            # print(count)
        if id in list and count < limit:

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



        else:
            print("Try again!")
            count += 1

    else:
        print("You have been blocked!,Try again after ",3,"minutes")
        Time = int(input("please enter finshed time: "))
        for T in range(0,Time):
            time.sleep(1)
            print(f"00:00:0{T}")
# maintomain()


