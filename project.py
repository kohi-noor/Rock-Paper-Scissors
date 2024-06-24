#Python program to code the rock, paper, scissors game
import random

while True:

    mylist = ["rock", "paper", "scissor"]
    you = input("You choose (Rock, Paper, Scissor): ")
    you = you.lower()
    rand_list = random.choice(mylist)

    print(f"The computer choose: {rand_list}")

    if you == rand_list:
        print("Draw!")
        cont = input("Wanna play again? (y/n): ")
        if cont == 'y':
            continue
        else:
            break

    elif you == 'paper' and rand_list== 'rock':
        print("You win!")
        cont = input("Wanna play again? (y/n): ")
        if cont == 'y':
            continue
        else:
            break    
    
    elif you == 'scissor' and rand_list== 'paper':
        print("You win!")
        cont = input("Wanna play again? (y/n): ")
        if cont == 'y':
            continue
        else:
            break    

    elif you == 'rock' and rand_list== 'scissor':
        print("You win!") 
        cont = input("Wanna play again? (y/n): ")
        if cont == 'y':
            continue
        else:
            break   

    else:
        print("You lose!")
        cont = input("Wanna play again? (y/n): ")
        if cont == 'y':
            continue
        else:
            break
        

