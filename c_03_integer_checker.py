

error = "Please enter an integer that is 13 or more."

try:
    my_num = int(input("Enter an integer: "))

    if my_num < 13:
        print(error)
    else:    
        print("Your number is", my_num)


except ValueError as ve:
    print(ve)
    print(error)