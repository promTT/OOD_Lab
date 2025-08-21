print("*** TorKham HanSaa ***")
commands = input("Enter Input : ").split(",")

lst = []    
for i in commands:
    command = i.split()
    if  command[0] == "X":
        break
    elif command[0] == "R":
        lst = []
        print("game restarted")
    elif command[0] == "P":
        word = list(command[1])
        if len(lst) == 0:
            lst.append(command[1])
            print(f"\'{command[1]}\' -> {lst}")
        else:
            temp = list(lst[-1])
            if temp[-1].lower() == word[1].lower() and temp[-2].lower() == word[0].lower():
                lst.append(command[1])
                print(f"\'{command[1]}\' -> {lst}")
            else:
                print(f"\'{command[1]}\' -> game over")
                break
    else:
        print(f"\'{i}\' is Invalid Input !!!")
        break
