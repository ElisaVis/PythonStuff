
def menu():
    while True:

        print("""

            __  __      _ __     ______                           __           
        / / / /___  (_) /_   / ____/___  ____ _   _____  _____/ /____  _____
        / / / / __ \/ / __/  / /   / __ \/ __ \ | / / _ \/ ___/ __/ _ \/ ___/
        / /_/ / / / / / /_   / /___/ /_/ / / / / |/ /  __/ /  / /_/  __/ /    
        \____/_/ /_/_/\__/   \____/\____/_/ /_/|___/\___/_/   \__/\___/_/     
                                                                            
        """)

        print("""
        [1]: Feet to Inches
        [2]: Inches to Feet
        [3]: Centimeters to Inches
        [4]: Inches to Centimeters
        [5]: Centimeters to Feet
        [6]: Feet to Centimeters
        [7]: EXIT
        """)
    

        option = int(input("[?]: "))

        if option == 1:
            feet = float(input("Input the amount of Feet: "))
            inches = feet * 12
            converted = print("Here is how many Inches that is: " + str(inches))

        if option == 2:
            inches = float(input("Input the amount of Inches: "))
            feet = inches / 12
            converted = print("Here is how many Feet that is: " + str(feet))

        if option == 3:
            centimeters = float(input("Input the amount of Centimeters: "))
            inches = centimeters / 2.54
            converted = print("Here is how many Inches that is: " + str(inches))

        if option == 4:
            inches = float(input("Input the amount of Inches: "))
            centimeters = inches * 2.54
            converted = print("Here is how many Centimeters that is: " + str(centimeters))

        if option == 5:
            centimeters = float(input("Input the amount of Centimeters: "))
            feet = centimeters / 30.48
            converted = print("Here is how many Feet that is: " + str(feet))

        if option == 6:
            feet = float(input("Input the amount of Feet: "))
            centimeters = feet * 30.48
            converted = print("Here is how many Centimeters that is: " + str(centimeters))

        if option == 7:
            exit()


menu()

