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