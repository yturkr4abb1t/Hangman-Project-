import random
import pyttsx3


# function to enable speech feedback from the computer 
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# function to generate a random word 
def wordlist():
    words = ["apple", "banana", "orange", "grape", 
             "kiwi", "mango", "pear", "pineapple", 
             "strawberry", "watermelon", 
             "spring", "summer", "fall", "winter", 
             "chocolate", "coding", "lollipop", 
             "caramel", "jellybean","bear", "peppermint", 
             "toffee", "taffy", "holiday"]

    return random.choice(words)

# function to display word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter # displays guessed letter(s)
        else:
            display += "_" # else displays blank 
    return display


def draw_hangman_body(attempts):
    if attempts == 6:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif attempts == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif attempts == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif attempts == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif attempts == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif attempts == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
    elif attempts == 0:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")
        
# ask user to play again 
def playagain():
    while True:
        answer = str(input("Run again? (y/n): "))
        if answer in ("y", "n"):
            if answer == "y":
                return True
    
            elif answer == "n":
                return False
        print("Goodbye")
        
# main function to run the game 
        
def hangman():
    while True: 
        print("Welcome to Hangman!")
        print("-------------------")
        speak("Welcome to Hangman!")
    
        chosen_word = wordlist() 
        guessed_letters = [] #temp variable to store a string
        attempts = 6
    
        word_display = display_word(chosen_word, guessed_letters)
        print("Word:", word_display)

        while attempts > 0:
        
            speak(f"Attempts left: {attempts}")
            print(f"Attempts left: {attempts}")
        
        
            guess = input("Guess a letter: ").lower()
            speak(f"You guessed: {guess}")
    
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    speak("You already guessed that letter: " + guess)
            
            # statement to reply for correct guess
                elif guess in chosen_word: 
                    speak("Good Guess!" + guess)
                    print("Good Guess!" + guess)
                
                    guessed_letters.append(guess) #append will add the letter to a list if not already present 
                
            #this will display the word as you guess
                    word_display = display_word(chosen_word, guessed_letters)
                    print("Word:", word_display)
                
            # statement to reply for incorrect guess 
                else:
                    speak( guess + " that letter is not in the word")
                    attempts -= 1
                
                    draw_hangman_body(attempts)


                 
            if set(guessed_letters) == set(chosen_word):
                speak(f"Congratulations! You guessed the word: {chosen_word}")
                break 
            if attempts == 0:
                speak(f"Sorry, you ran out of attempts. The word was: {chosen_word}")
    
        if not playagain():
            break
            

if __name__ == "__main__":
    hangman()

                
            
            
            
    
    
    