p1 = input("Player1: Enter choice \n")
p2 = input("Player2: Enter choice \n")

if (p1 == "Rock" and p2 == "Scissor"):
    print("P1 wins")
elif (p1 == "Paper" and p2 == "Rock"):
    print("P1 wins")
elif (p1 == "Scissor" and p2 == "Rock"):
    print("P2 wins")
elif (p1 == p2):
    print("It's a tie")



# roll = random.randint(1,6)
# guess = int(input("Guess a dice roll \n"))
# if guess == roll:
#     print("Correct! They rolled a " + str(roll))
# else:
#     print("Wrong! They rolled a " + str(roll))

