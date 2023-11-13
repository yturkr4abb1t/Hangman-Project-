# example code to source from - https://www.makeuseof.com/python-game-hangman-create/?utm_source=flipboard&utm_content=topic%2Fadventuregame#:~:text=Begin%20the%20game%20by%20displaying,whether%20it%20is%20an%20alphabet
# link to the github from the website above - https://github.com/makeuseofcode/Hangman-Game/blob/main/hangman.py

######################################################

import pyttsx3
import speech_recognition as sr
import random 

#[the following code has been coded by Yildizay - 

# Speech Recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

#speak function 
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

# to display the word as guessed 
def display_word(word, guessed_letters):
    display = "" # this sets it like fresh 
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
        return display 

def draw_hangman(attempts):
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

def main():

    speak("Welcome to Hangman! A word will be chosen randomly for you to guess, good luck!")

# [ def get_random_word_from_wordlist():
   # wordlist = []
    #with open("hangman_wordlist.txt", 'r') as file:
       # wordlist = file.read().split('\n')
   # word = random.choice(wordlist)
    #return word ]
# --------------------------- 
# [   word = get_random_word_from_wordlist()
   # temp = get_some_letters(word)
    #chances = 7
   # found = False
   # while True: ] 

# below is my code ive engineered from this source code snippet above. 
# instead of a seperate word file that the code above would call from, Ive placed them in a set list. 

hangman_wordlist = ["cherry", "apple", "biology", "spring", "summer", "winter"]

# picks random word 
word = random.choice(hangman_wordlist)
guessed_letters = ["_"] * len(word)
attempts = len(hangman_wordlist) - 1
# or attempts = 7 

word_found = False

while True:

    # [ def get_some_letters(word):
    #letters = []
    #temp = '_'*len(word)
    #for char in list(word):
        #if char not in letters:
            #letters.append(char)
    #character = random.choice(letters)
    #for num, char in enumerate(list(word)):
        #if char == character:
            #templist = list(temp)
            #templist[num] = char
            #temp = ''.join(templist)
    #return temp ] 

# below is my code ive engineered from this source code snippet above 
# instead of the large portion of code that would take it from the terminal user input,
# it will get it form the microphone and append it to a list

        with microphone as source:
            audio = recognizer.listen(source)

        guessed_letter = recognizer.recognize_google(audio)

        # [ print(temp, end='')
        #print(f"\t(word has {len(word)} letters)")
        #print(f"Chances left: {chances}")
        #character = input("Enter the character you think the word may have: ")
        #if len(character) > 1 or not character.isalpha():
            #print("Please enter a single alphabet only") ] 

# the code snippet above was my guide in coding my version below: using .alpha but adding .lower to make it case sensitive. 

        if guessed_letter.isalpha() and len(guessed_letter) == 1:
                guessed_letter = guessed_letter.lower()

                if guessed_letter in guessed_letters:
                    speak("You already guessed that letter.")


                elif guessed_letters in word:
                    guessed_letters.append(guessed_letter) # this will append or add the letter to the list to keep track of letters
                    current_display = display_word(word, guessed_letters)  

# set will compare the letters to the chosen word to check if they have been guessed correctly, if True the user wins

                    if set(guessed_letters) == set(word):
                        speak("Congratulations! You guessed the word: " + word)
                        break

        
                else:
                    attempts -= 1
                    speak("Incorrect guess. You have {} attempts left.".format(attempts))

        else:
                speak("Please guess a single letter.")
                
                if attempts == 0:
                    speak("Game over! The word was: " + word)

# else will continute the game drawing the figure 
                else:
                    draw_hangman(attempts)
                    print()

# indent error - fix 
#except sr.UnknownValueError:
#speak("Sorry, I didn't catch that. Please try again.")

if __name__ == "__main__":
   main()
