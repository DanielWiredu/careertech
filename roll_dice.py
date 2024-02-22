import random

comp_choice = random.choice(['Rock','Paper','Scissors'])
user_input = input("Enter your choice")

if (comp_choice == "Rock" and user_input == "Scissor"):
    print("P1 wins")
elif (comp_choice == "Paper" and user_input == "Rock"):
    print("P1 wins")
elif (comp_choice == "Scissor" and user_input == "Rock"):
    print("P2 wins")
elif (comp_choice == user_input):
    print("It's a tie")



    #gillianogyiri@gmail.com
    # Gillian  Ogyiri
    # https://www.youtube.com/watch?v=KhGWbt1dAKQ
    # https://www.youtube.com/watch?v=pBy1zgt0XPc
    # https://www.youtube.com/watch?v=i_23KUAEtUM

