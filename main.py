def project_one():
    while True:

        user_input = int(input("Hi, user! Please enter the number relating to each option to begin: ""(1 = temp, 2 = weight, 3 = distance, 4 = height, 5 = time, 0 = Quit): "))

        if user_input == 1:
            print("Okay, let's convert temperature in Fahrenheit to Celsius")
            temp = float(input("Enter temperature in fahrenheit: "))
            formula1 = (temp - 32) * 5 / 9
            print(f"{temp} degrees fahrenheit is {formula1} degrees in celcius")

        elif user_input == 2:
            print("Okay, let's convert weight in Pounds to Kilograms")
            weight = float(input("Enter weight in pounds: "))
            formula2 = (weight * 0.453592)
            print(f"{weight} pounds in is {formula2} kilograms")

        elif user_input == 3:
            print("Okay, let's convert distance in Feet to Meters")
            distance = float(input("Enter distance in feet: "))
            formula3 = (distance * 0.3048)
            print(f"{distance} feet in {formula3} meters")   

        elif user_input == 4:
            print("Okay, let's convert inches to feet")
            height = int(input("Enter height in inches: "))
            feet = height // 12 
            inches = height % 12 
            print(f"{height} inches is equal to {feet} feet and {inches} inches.")

        elif user_input == 5:
            print("Okay, let's convert minutes to hours and minutes")
            time = int(input("Enter time in minutes: ")) 
            hours = time // 60  
            minutes = time % 60 
            print(f"{time} minutes is equal to {hours} hours and {minutes} minutes.")

        elif user_input == 0:
            print("Goodbye for now!")
            break

        else:
            print("Please enter a valid number")

project_one()


