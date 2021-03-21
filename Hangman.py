# This is a hangman game.
# Created for learning.

def display_hangman(tries):
    guess0 = ""
    guess1 = """\n    _____\n   /     \\\n"""
    guess2 = """\n      |\n      |\n      |\n    __|__\n   /     \\\n"""
    guess3 = """\n      _______\n      |\n      |\n      |\n    __|__\n   /     \\\n"""
    guess4 = """\n      _______\n      |/\n      |\n      |\n    __|__\n   /     \\\n"""
    guess5 = """\n      _______\n      |/    |\n      |\n      |\n    __|__\n   /     \\\n"""
    guess6 = """\n      _______\n      |/    |\n      |     O\n      |\n    __|__\n   /     \\\n"""
    guess7 = """\n      _______\n      |/    |\n      |     O\n      |     |\n    __|__\n   /     \\\n"""
    guess8 = """\n      _______\n      |/    |\n      |     O\n      |    /|\n    __|__\n   /     \\\n"""
    guess9 = """\n      _______\n      |/    |\n      |     O\n      |    /|\\\n    __|__\n   /     \\\n"""
    guess10 = """\n      _______\n      |/    |\n      |     O\n      |    /|\\\n    __|__  /\n   /     \\\n"""
    guess11 = """\n      _______\n      |/    |\n      |     O\n      |    /|\\\n    __|__  / \\\n   /     \\\n"""

    arr = [guess0, guess1, guess2, guess3, guess4, guess5, guess6, guess7, guess8, guess9, guess10, guess11]
    print(arr[tries])

print("This is a hangman game.")
def get_word():
    word = input("Please enter a word to be guessed: ")
    for n in range(30):
        print("\n")

    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_word = []
    guessed_letter = []
    tries = 0

    print("Let's play a game of Hangman!")
    display_hangman(tries)
    print(word_completion)

    while not guessed and tries < 11:
        guess = input("Enter a letter or a word: ").upper()

        if len(guess) == 1 and guess.isalpha():

            if guess in guessed_letter:

                print("You've already guessed that letter.")

            elif guess not in word:

                print(guess, "is not in the word.")

                tries += 1
                guessed_letter.append(guess)

            else:
                print(guess, "is in the word.")

                guessed_letter.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess

                word_completion = "".join(word_as_list)

                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():

            if guess in guessed_word: 

                print("You've already guessed the word", guess)

            elif guess != word:

                print(guess, "is not the word.")

                tries += 1
                guessed_word.append(guess)

            else:

                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")

        display_hangman(tries)
        print(word_completion)
        print("\n")

    if guessed:
        print("You've guessed the right word.")
    else:
        print("You ran out of tries. The word was ", word)

def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N) ".upper() == "Y"):
            word = get_word()
            play(word)

if __name__ == "__main__":
    main()

        


