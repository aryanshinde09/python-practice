
import random
rand = random.randint(1,3)

try:
    user = int(input("Pick rock(1), paper(2), scissor(3):"))
    print("-------------------------------------------------------------------------")
    match (user,rand):
            case (1,1):
                print("Draw both Choose Rock")
            case (1,2):
                print("Comp wins! as it chose paper")
            case (1,3):
                print("user win! as comp chose scissor")
            case (2,1):
                print("user win! as comp chose rock")
            case (2,2):
                print("Draw! both chose paper")
            case (2,3):
                print("comp win! as it chose scissor ")
            case (3,1):
                print("Comp win! as it choose rock")
            case (3,2):
                print("user win! as comp chose paper")
            case (3,3):
                print("Draw! both choose scissor")
            case _ :
                print("Enter number 1 to 3!")
except:
    print("----------------------------------------------------")
    print("That was not a valid number!")
    print("----------------------------------------------------")

