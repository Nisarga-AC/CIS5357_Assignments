import random

u_num = int(input("Guess a number between 1 to 10: "))
w_num = random.uniform(1, 10) // 1

for i in range(3):
    if u_num == w_num:
        print(f"Congrats you win and you guessed this number in {i+1} tries!")
        break
    elif u_num < w_num:
        if i == 2:
            print("That is too low, sorry you are out of turns")
            break
        else:
            print("That is too low")
    else:
        if i == 2:
            print("That is too high, sorry you are out of turns")
            break
        else:
            print("That is too high")

    u_num = int(input("Guess again: "))
