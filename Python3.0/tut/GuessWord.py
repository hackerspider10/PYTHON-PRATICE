# Guess the word
secret_word = "joker"
guess = ""
guess_count = 0
guess_limit = 3
out_guesses = False
while guess != secret_word and not out_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_guesses = True

if out_guesses:
    print("Out of guesses, You lose!")
else:
    print("You win!!")
