command =" "
started =False
stop =False
while True :
    command =input(">").lower()
    if command == "start" :
        if started :
            print("Car is already running")
        else:
            started=True
            print("Car started. Ready to go!")

    elif command =="stop" :
        if stop :
            print("Car is already stopped")
        else:
            stop=True
            print("Car Stopped")
    elif command== 'help' :
        print('''
start -to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command =="quit" :
        break
    else:
        print("Sorry I do not understand.")