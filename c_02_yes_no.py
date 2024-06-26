
# check users enter yes (y) or no (n)
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You did not choose a valid response")

def main():
    # main routine
    want_instructions = yes_no("Do you want to read the instructions? ")
    print(f"You chose {want_instructions}")

    roll_again = yes_no("Do you want to roll again? ")
    print(f"You said {roll_again} to rolling again. ")

if __name__ == "__main__":
    print('Coming at your from c_02_yes_no.py')