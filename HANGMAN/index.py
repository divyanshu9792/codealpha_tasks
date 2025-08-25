import random

def hangman_game():
    words = ["python", "hangman", "program", "computer", "keyboard"]
    secret_word = random.choice(words).lower()
    guessed_letters = []
    attempts_left = 6
    word_progress = ["_"] * len(secret_word)
    
    print("Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters. You have {attempts_left} attempts to guess it.")
    print(" ".join(word_progress))
    
    while attempts_left > 0 and "_" in word_progress:
        guess = input("Guess a letter: ").lower()
        
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
            
        guessed_letters.append(guess)
        
        if guess in secret_word:
          
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    word_progress[i] = guess
            print("Correct!")
        else:
            attempts_left -= 1
            print(f"Wrong! You have {attempts_left} attempts left.")
            
       
        print(" ".join(word_progress))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
    
 
    if "_" not in word_progress:
        print(f"Congratulations! You guessed the word: {secret_word}")
    else:
        print(f"Game over! The word was: {secret_word}")

if __name__ == "__main__":
    hangman_game()