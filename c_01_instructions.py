
# check users enter yes (y) or no (n)
def yes_no(question):
    '''Capture a valid yes (y) or no (n) response from the user'''
    
    while True:
        response = input(question).lower()

        # Checks user response to y/n question
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

def instructions():
    '''Prints game instructions'''
    print('''
**** Instructions ****

Instructions to go here.      
''')


# main routine
print("\n🎲🎲 Roll it 13 🎲🎲\n")

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == 'yes':
    instructions()

print('continue...')


# if __name__ == "__main__":
#     instructions()