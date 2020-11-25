# The hangman game
import random

words = ["lion", "cat", "tower", "computer", "router", "speaker", "castle", "soup", "keyboard", "mouse", "telephone", "smartphone", "television", "light", "yellow"]
random_number = random.randint(0, len(words))
random_word = words[random_number - 1]

word_in_game = []
for i in range(len(random_word)):
    word_in_game.append("_")


def check_did_letter(keyboard_input):
    try:
        if ord(keyboard_input) >= 97 and ord(keyboard_input) <= 122:
            pass
        else:
            print(" ")
            print("Use letter nothing else")
    except:
        print(" ")
        print("You can type just one letter")
    return x

print("=" * 50, "\n")
print("Welcome to Hangman game!!!")
print(" ")
print("this word have", (len(random_word)), "letters")

guess = ""
x = 6
while True:
    print(" ")
    print("=" * 50)
    guess = input("pick a letter: ").lower()
    check_did_letter(guess)


    if guess in random_word:
        for letter in range(len(random_word)):
            if random_word[letter] == guess:
                word_in_game[letter] = guess
        for i in range(len(random_word)):
            print(word_in_game[i], end=" ")
        print(" ")
        print("The letter is in word!", end=" ")

    else:
        x -= 1
        print(" ")
        print("Wrong letter! You have", x ,"more attempt/s", end=" ")
        
    if "_" not in word_in_game:
        print(" ")
        print("Congratulation!!! You are the winner :)")
        break
    elif x == 0:
        print(" ")
        print("You lost :( The word was:", random_word)
        break