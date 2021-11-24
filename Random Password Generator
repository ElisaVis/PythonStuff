import random

def randPassword():
    while True:

        print("""
    ____  ___   ___________       ______  ____  ____     _____________   ____________  ___  __________  ____ 
   / __ \/   | / ___/ ___/ |     / / __ \/ __ \/ __ \   / ____/ ____/ | / / ____/ __ \/   |/_  __/ __ \/ __ \
  / /_/ / /| | \__ \\__ \| | /| / / / / / /_/ / / / /  / / __/ __/ /  |/ / __/ / /_/ / /| | / / / / / / /_/ /
 / ____/ ___ |___/ /__/ /| |/ |/ / /_/ / _, _/ /_/ /  / /_/ / /___/ /|  / /___/ _, _/ ___ |/ / / /_/ / _, _/ 
/_/   /_/  |_/____/____/ |__/|__/\____/_/ |_/_____/   \____/_____/_/ |_/_____/_/ |_/_/  |_/_/  \____/_/ |_|  
             Created by YeetSauce676                                                                                               
        """)

        print("""
        [1]: Password Generator
        [2]: Exit
        """)

        option = int(input("[?]: "))

        if option == 1:
           print("Dont forget to write down the password somewhere secure")
           passlen = int(input("How long would you like your password to be?: "))
           characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&"
           passList = [random.choice(characters) for i in range(passlen)]
           password = "".join(passList)
           print(password)

        if option == 2:
            exit()

randPassword()
