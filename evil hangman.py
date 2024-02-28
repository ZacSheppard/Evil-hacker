#evil hang man

#picks random evil word
#player guesses a letter/word
#checks if letter is in evil word
#display the evil word with the guessed letters


def generate_secret_word():
    #chooses evil word to use for the game
    word = "hacker"
    return word

def get_player_guess():
    #must be alphanumeric a-z, 0-9
    #must be == 1 character in length 
    guess = input("please guess a letter:    ")
    while len(guess) != 1 or guess.isdigit():
        guess = input("you can only do single letters and cant do numbers dumbass, try again")
    print(f"accepted luh letter: {guess}")
    return guess

def display_word_to_guess(secret_word, guesses):
    displayed_word = ""
    for letter in secret_word:
        if letter in guesses:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


def check_if_won(secret_word, guesses):
    for letter in secret_word:
        if letter not in guesses:
            return False
    return True

def main():
    secret_word = generate_secret_word()
    guesses = []
    attempts = 10

    while attempts > 0 and not check_if_won(secret_word, guesses):
        print(display_word_to_guess(secret_word, guesses))
        guess = get_player_guess()
        if guess not in secret_word:
            attempts -= 1
        guesses.append(guess)
        print(f"attempts remaining: {attempts}")

    if check_if_won(secret_word, guesses):
        print("congratulations, you evil as hell")
    else:
        print("out of attempts, you DIE! the wor was", secret_word)


main()

    
