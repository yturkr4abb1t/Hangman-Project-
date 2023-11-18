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
             "chocolate", "gummy bears", "lollipop", 
             "caramel", "jellybean","licorice", "peppermint", 
             "toffee", "taffy", "gumdrop"]

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

# def drawhangman():
    
    
    
def hangman():
    print("Welcome to Hangman!")
    print("-------------------")
    speak("Welcome to Hangman!")
    
    
    chosen_word = wordlist() 
    guessed_letters = [] #temp variable to store a string
    attempts = len(chosen_word) - 1
    
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
                
                word_display = display_word(chosen_word, guessed_letters)
                print("Word:", word_display)
                
            # statement to reply for incorrect guess 
            else:
                speak( guess + " that letter is not in the word")
                attempts -= 1
        else:
            speak("that letter is not in the word")
                 
        if set(guessed_letters) == set(chosen_word):
            speak(f"Congratulations! You guessed the word: {chosen_word}")

        elif attempts == 0:
            speak(f"Sorry, you ran out of attempts. The word was: {chosen_word}")

if __name__ == "__main__":
    hangman()

                
            
            
            
    
    
    
