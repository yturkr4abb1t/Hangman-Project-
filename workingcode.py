import pyttsx3
import speech_recognition as sr
import random

class Hangman:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def choose_word(self):
        words = ["python", "hangman", "computer", "programming", "developer", "language"]
        return random.choice(words)

    def display_word(self, word, guessed_letters):
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def hangman(self):
        chosen_word = self.choose_word()
        guessed_letters = []
        total_attempts = 6
        attempts = 0

        self.speak("Welcome to Hangman!")
        print("Welcome to Hangman!")
        print(self.display_word(chosen_word, guessed_letters))

        while True:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.pause_threshold = 1
                audio = self.recognizer.listen(source)

            try:
                print("Recognizing...")
                query = self.recognizer.recognize_google(audio, language='en-in')
                print(query)
                guess = query.lower()
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that. Please repeat.")
                self.speak("Please repeat")
                continue

            if len(guess) != 1 or not guess.isalpha():
                self.speak("Please say a valid single letter.")
                print("Please say a valid single letter.")
                continue

            if guess in guessed_letters:
                self.speak("You already guessed that letter. Try again.")
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            if guess not in chosen_word:
                attempts += 1
                print(f"Incorrect guess. {total_attempts - attempts} attempts remaining.")

            print(self.display_word(chosen_word, guessed_letters))

            if set(guessed_letters) == set(chosen_word):
                print("Congratulations! You guessed the word!")
                break

            if attempts == total_attempts:
                print(f"Sorry, you're out of attempts. The word was: {chosen_word}")
                break

if __name__ == "__main__":
    hangman_game = Hangman()
    hangman_game.hangman()
