def Topper(regno):

    ods = 0
    evs = 0

    for i in range(len(regno)):
        if int(regno[i]) % 2 == 0:
            evs += int(regno[i])
        else:
            ods += int(regno[i])

    if ods == evs:
        print("true")
    else:
        print("false")
    
regno = input()
print(Topper(regno))