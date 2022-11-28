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