import os
import time
import sys

action = None
duration = 0

#For Windows
if sys.platform == "win32":
    while action == None:
        try:
            choice = int(input("Choose action (1: Shutdown |2: Restart |3: Sleep): "))
        except ValueError:
            print("Invalid input. Please choose the number indicating the operation.")
            continue
        if choice in (1, 2, 3):
            if choice == 1:
                action = "shutdown /s /t 0"
            elif choice == 2:
                action = "shutdown /r /t 0"
            elif choice == 3:
                action = "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
        else:
            print("Out of range")
            continue
    
    while duration == 0:
        try:
            choice = int(input("Enter time in seconds until action: "))
        except ValueError:
            print("Invalid input")
            continue
        if choice <= 0:
            print("Time can not be less or equal to zero")
            continue
        duration = choice

    canceled = False

    try:
        for sec in range(duration, 0, -1):
            print(f"{sec} seconds until {action}. Press Ctrl+C to cancel")
            time.sleep(1)

    except KeyboardInterrupt:
        canceled = True
        print(f"\n{action} canceled by user.")

    if not canceled:
        os.system(action)


#For Linux
elif sys.platform.startswith("linux"):
    while action == None:
        try:
            choice = int(input("Choose action (1: Shutdown |2: Restart |3: Sleep): "))
        except ValueError:
            print("Invalid input. Please choose the number indicating the operation.")
            continue
        if choice in (1, 2, 3):
            if choice == 1:
                action = "systemctl poweroff"
            elif choice == 2:
                action = "systemctl reboot"
            elif choice == 3:
                action = "systemctl suspend"
        else:
            print("Out of range")
            continue
    
    while duration == 0:
        try:
            choice = int(input("Enter time in seconds until action: "))
        except ValueError:
            print("Invalid input")
            continue
        if choice <= 0:
            print("Time can not be less or equal to zero")
            continue
        duration = choice


    canceled = False

    try:
        for sec in range(duration, 0, -1):
            print(f"{sec} seconds until {action}. Press Ctrl+C to cancel")
            time.sleep(1)

    except KeyboardInterrupt:
        canceled = True
        print(f"\n{action} canceled by user.")

    if not canceled:
        os.system(action)
