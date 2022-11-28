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