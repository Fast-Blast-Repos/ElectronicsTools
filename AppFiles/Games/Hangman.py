# imports
import random as rd
import time as t

# random colors for print
def RandomColors(text, weight):
    # if you are reading this, you have to make this code prettier

    # initialise color lists
    R = ["\33[0;49;31m", "\33[1;49;31m", "\33[2;49;31m", "\33[3;49;31m", "\33[4;49;31m", "\33[5;49;31m", "\33[6;49;31m", "\33[7;49;31m"]
    G = ["\33[0;49;32m", "\33[1;49;32m", "\33[2;49;32m", "\33[3;49;32m", "\33[4;49;32m", "\33[5;49;32m", "\33[6;49;32m", "\33[7;49;32m"]
    Y = ["\33[0;49;33m", "\33[1;49;33m", "\33[2;49;33m", "\33[3;49;33m", "\33[4;49;33m", "\33[5;49;33m", "\33[6;49;33m", "\33[7;49;33m"]
    N = ["\33[0;49;34m", "\33[1;49;34m", "\33[2;49;34m", "\33[3;49;34m", "\33[4;49;34m", "\33[5;49;34m", "\33[6;49;34m", "\33[7;49;34m"]
    P = ["\33[0;49;36m", "\33[1;49;36m", "\33[2;49;36m", "\33[3;49;36m", "\33[4;49;36m", "\33[5;49;36m", "\33[6;49;36m", "\33[7;49;36m"]
    C = ["\33[0;49;37m", "\33[1;49;37m", "\33[2;49;37m", "\33[3;49;37m", "\33[4;49;37m", "\33[5;49;37m", "\33[6;49;37m", "\33[7;49;37m"]

    # initialise variables
    OUT = []
    txt = list(text)
    y = 0

    # add random color to each character in the text
    for x in range(len(txt)):
        random = rd.randint(0, 5)
        if random == 0:
            OUT.append(R[weight] + txt[y])
        elif random == 1:
            OUT.append(G[weight] + txt[y])
        elif random == 2:
            OUT.append(Y[weight] + txt[y])
        elif random == 3:
            OUT.append(N[weight] + txt[y])
        elif random == 4:
            OUT.append(P[weight] + txt[y])
        elif random == 5:
            OUT.append(C[weight] + txt[y])
        y += 1

    # joins and returns the output
    return ''.join(OUT) + "\033[0m"

# hangman states
states = ["""______
|    |
|    O
|   /|\\
|   / \\
|_______
""","""______
|    |
|    O
|   /|\\
|   /
|_______
""","""______
|    |
|    O
|   /|\\
|   
|_______
""","""______
|    |
|    O
|   /|
|   
|_______
""","""______
|    |
|    O
|    |
|   
|_______
""","""______
|    |
|    O
|   
|   
|_______
""","""______
|    |
|    
| 
|  
|_______
"""]

# Load words from words.txt into a list
with open("AppFiles/GameAssets/words.txt", "r") as file:
    words = [line.strip() for line in file if line.strip()]

# initiate variables
word = rd.choice(words)
lives = 7
char_list = list(word)
guesso = ["-"] * len(word)
guessed = [""]
win = ["You win!", "Congratulations!", "Great job!", "You did great!", "Nice work!", "You're a winner!", "You did it!", "You're amazing!", "You're unstoppable!", "You're a true champion!", "Spectacular!"]

print(RandomColors("Hangman!", 1))

# main game loop
while lives > 1:
    print(RandomColors("".join(guesso), 0))
    print(RandomColors(states[lives-1], 0))
    print(RandomColors("Guessed letters:" + " ".join(guessed), 0))
    guess = input(RandomColors("Guess a letter: ", 0)).lower()
    if len(guess) != 1 or not guess.isalpha():
        print(RandomColors("Please enter a single letter.", 0))
    elif guess in guessed:
        print(RandomColors("You already guessed that letter.", 0))
    elif guess in char_list:
        print(RandomColors("Correct!", 0))
        guessed.append(guess)
        for i, char in enumerate(char_list):
            if char == guess:
                guesso[i] = guess
    else:
        print(RandomColors("Incorrect!", 0))
        guessed.append(guess)
        lives -= 1
    if "-" not in guesso:
        print(RandomColors("You guessed the word:" + word, 0))
        # print a random winning message
        message = rd.choice(win)
        for i in range(20):
            print(RandomColors(message, 7))
            t.sleep(0.1)
        break

# if lost
if lives == 1:
    print(RandomColors(states[0], 0))
    print(RandomColors("You lost! The word was: " + word, 0))