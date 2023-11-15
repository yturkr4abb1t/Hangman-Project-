import pyttsx3 
import speech_recognition as sr 
import random



# speech recog 
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# speak function 
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
    
def display(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display 

def draw_hangman():
    
    
    
def main():
    hangman_list = ["cherry", "summer", "spring"]
    
    word = random.choice(hangman_list)
    guessed_letters = ["_"] * len(word)
    attempts = 7 
    
    
    guessed_letters = []
    
    speak("welcome to hangman! guess a letter")
    while True:
    
        with microphone as source:
            audio = recognizer.listen(source)
    
        guessed_letter = recognizer.recognize_google(audio)
    
        if guessed_letter.isalpha() and len(guessed_letter) == 1:
            guessed_letter = guessed_letter.lower()
        
            if guessed_letter in guessed_letters:
                speak("you already guessed that letter, try again")
            
        elif guessed_letters in word:
# code below will add letters to list and keep track
            guessed_letters.append(guessed_letter)
            current_display = display(word, guessed_letters)
            
            if set(guessed_letters) == set(word):
                speak("you win, the word was:" + word)
                break 
            
            else: 
                attempts -= 1
            speak(" incorrect guess. you have {} attempts left" .format(attempts))
            
            
# code below will run if they say multiple letters at once
        else: 
            speak("please guess a single letter")
            
        if attempts == 0:
            speak("game over, the word was:" + word)
            
        else: 
            draw_hangman(attempts)
            print()
            
            
        
        
        
        
    
            
            
    