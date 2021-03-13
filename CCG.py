import random as r


def play():
    colors = {'Red':0, 'Yellow':1, 'Orange':2, 'Green':3, 'Blue':4}

    player_choice = int(input("""\nChoose a color:
Red = 0
Yellow = 1
Orange = 2
Green = 3
Blue = 4

->"""))

    if player_choice < 0 or player_choice > 4:
        return -1

    com_choice = r.choice(list(colors.keys()))

    print(f"""\nYou choose: {list(colors.keys())[list(colors.values()).index(player_choice)]}
Computer choose: {com_choice}\n""" )

    if player_choice == int(colors.get(com_choice)):
        return 1
    else:
        return 0



print("""Rule:
If the player guesses the same color as the computer, player gets a point.
Otherwise the computer gets the point!""")
play_choice = input("""\nDo you want to play the game:
Yes: Y
No: N

->""").lower()

player_score = 0
comp_score = 0

try:
    while play_choice != 'n':
        c = play()
        if c == 1:
            player_score += 1
            print(f"""\nPlayer Score = {player_score}
Computer Score = {comp_score}""")
        elif c == 0:
            comp_score += 1
            print(f"""\nPlayer Score = {player_score}
Computer Score = {comp_score}""")
        else:
            print("\nEnter a Valid Choice!")
            print(f"""\nPlayer Score = {player_score}
Computer Score = {comp_score}""")

        play_choice = input("""\nDo you want to play the game again:
Yes: Y
No: N

->""").lower()

    if player_score > comp_score:
        print("You Won!")
    elif player_score < comp_score:
        print("You Lost!")
    else:
        print("Tie!")
    print("\nThank You!")

except:
    print("Something went wrong!")