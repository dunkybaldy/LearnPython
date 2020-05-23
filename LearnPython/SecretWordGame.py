secret_word = "Giraffe"
guess_limit = 5
guess_count = 0
guess = ""
has_guesses = True

while guess != secret_word and has_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ").lower()
        guess_count += 1
    else:
        has_guesses = False

if has_guesses:
    print("You win!")
else:
    print(f"You lose! The word was '{secret_word}'")
