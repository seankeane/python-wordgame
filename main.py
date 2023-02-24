import re
import random
import time

# get word list file present on Unix systems
words_file = open("/usr/share/dict/words", "r").readlines()
# populate list variable with all 5-letter words with line break character removed
wordlist = []
for sub in words_file:
    if len(sub) == 6:
        wordlist.append(sub.replace("\n", ""))
# select an answer at random from the list
n = random.randint(0, len(wordlist))
answer = wordlist[n]

# print out game instructions
print("Try to guess the 5-letter word.\nHow to play:")
print("After each guess a key will show to indicate how close your are to guessing the word e.g. x+--x")
print("+ means the letter in that position in the word you guessed is also in the same position in the answer.")
print("- means the letter in that position in the word you guessed is also in the answer but in a different position.")
print("x means the letter in that position is not present in the answer.\nGood Luck! The timer has started.")


def check_only_alpha(check):
    x = re.search(r"^[A-Za-z]*$", check)
    return False if x is None else True


is_solved = False
start_time = time.time()
guess = ""
while not is_solved:
    if guess.lower() == answer.lower():
        is_solved = True
        break

    guess = input("Enter your guess:\n")

    if len(guess) != 5:
        guess = input("Enter a 5-letter word please:\n")

    if not check_only_alpha(guess):
        guess = input("Your guess should only contain letters. Try again please:\n")

    if guess not in wordlist:
        guess = input("That is not a valid word. Try again:\n")

    res = ""
    for index, val in enumerate(guess):
        if val == answer[index]:
            res += "+"
        elif val in answer:
            res += "-"
        else:
            res += "x"
    print(res)

print("WHOOP!! It was {}.".format(answer))
print("It took you {} seconds to find the word.".format(round(time.time() - start_time), 2))
