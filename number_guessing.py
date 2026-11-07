import random 
iterations = 0
exception = 0

while True:
    try:
        comp = random.randint(1, 10)
        user = int(input("Enter a number between 1 to 10:"))

        if user > 10:
            raise ValueError
        elif comp == user:
            print("You guessed it right!")
            break
        else:
            print("You guessed it wrong! The correct number was", comp)
        print("-------------------------------------------------------------------")
        iterations += 1
 
    except ValueError:
        print("Enter a valid number from 1 to 10")
        print("-------------------------------------------------------------------")
        exception += 1
        

print("***************************************")
print(f"You guessed in {iterations} Attempt.")
print(f"You had provided {exception} non integer value. which did not count in total attempt")










