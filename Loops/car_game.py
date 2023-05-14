command = ""
started = False
while True:
    command = input(">> ").lower()
    if command == "start":
        if started == True:
            print("Car is already Started")
        else:
            started = True    
            print("Car is Started")
    elif command == "stop":
        if started == False:
            print("Car is already Stoped")
        else:
            started = False
            print("Car is Stpoed")
    elif command == "help":
        print('''
            start - for start car
            stop - for stop 
            quit - for exit program 
              ''') 
    elif command == "quit":
        print("you Quit the programe")
        break  
    else:
        print("Not a valid key Press help")