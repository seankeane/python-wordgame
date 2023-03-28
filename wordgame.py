import re
import random
import time


def make_wordlist():
    # get word list file present on Unix systems
    words_file = open("/usr/share/dict/words", "r").readlines()
    words = []
    for sub in words_file:
        # check for only 5-letter words and words that do not start with uppercase
        if len(sub) == 6 and re.search(r"^[a-z]*$", sub[0]) is not None:
            words.append(sub.replace("\n", ""))
    return words


def make_answer():
    n = random.randint(0, len(wordlist))
    ans = wordlist[n]
    return ans


def print_instructions():
    print("Try to guess the 5-letter word.\nHow to play:")
    print("After each guess a key will show to indicate how close your are to guessing the word e.g. x+--x")
    print("+ means the letter in that position in the word you guessed is also in the same position in the answer.")
    print(
        "- means the letter in that position in the word you guessed is also in the answer but in a different position.")
    print("x means the letter in that position is not present in the answer.\nGood Luck! The timer has started.")


def ask_for_guess():
    global num_guesses, guess
    num_guesses += 1
    guess = input("Enter your guess:\n")


def check_only_alpha(check):
    x = re.search(r"^[A-Za-z]*$", check)
    return False if x is None else True


def check_is_solved(g, a):
    return g.lower() == a.lower()


def check_is_valid_guess(g):
    if len(g) != 5:
        print("Enter a 5-letter word please.")
        return False
    elif not check_only_alpha(g):
        print("Your guess should only contain letters.")
        return False
    elif g.lower() not in wordlist:
        print("That is not a valid word.")
        return False
    else:
        return True


def print_key(g):
    res = ""
    for index, val in enumerate(g):
        if val.lower() == answer[index]:
            res += "+"
        elif val.lower() in answer:
            res += "-"
        else:
            res += "x"
    print(res)


def print_letters(g):
    global letters
    for letter in g:
        letters = letters.replace(letter.lower(), "-")
    print(f"Letters you haven't guessed: {letters}")


def print_congrats():
    final_time = round((time.time() - start_time), 2)
    print(f"WHOOP!! It was {answer}.")
    print(f"It took you {final_time} seconds and {num_guesses} guesses to find the word.")


if __name__ == "__main__":
    is_solved = False
    num_guesses = 0
    start_time = time.time()

    wordlist = make_wordlist()
    answer = make_answer()
    print_instructions()

    letters = 'abcdefghijklmonpqrstuvwxyz'
    guess = ""
    while not is_solved:
        if num_guesses > 0:
            if check_is_valid_guess(guess):
                if check_is_solved(guess, answer):
                    is_solved = True
                    print_congrats()
                else:
                    print_key(guess)
                    print_letters(guess)
                    ask_for_guess()
            else:
                ask_for_guess()
        else:
            ask_for_guess()