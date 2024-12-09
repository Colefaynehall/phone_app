import time
import random
from playsound import playsound
import os
import pyttsx3

# Initialize TTS engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 100)  # Slower speed
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[0].id)  # Use the first voice

# Text-to-Speech Response
def speak_response(message):
    """Speak a text response using TTS."""
    print(f"TTS: {message}")
    tts_engine.say(message)
    tts_engine.runAndWait()

# Magic 8-Ball Feature
def magic_8_ball():
    responses = [
        "It is certain.",
        "Ask again later.",
        "My sources say no.",
        "Outlook good.",
        "Very doubtful."
    ]
    speak_response(random.choice(responses))

# Choose Your Own Adventure Game
def adventure_game():
    speak_response("Welcome to the adventure. Do you take the path left or right?")
    choice = input("Enter 1 for left or 2 for right: ")
    if choice == "1":
        speak_response("You encounter a dragon! Do you fight or run?")
        sub_choice = input("Enter 1 to fight or 2 to run: ")
        if sub_choice == "1":
            speak_response("You bravely fight and win! Congratulations.")
        else:
            speak_response("You ran away safely. Maybe next time!")
    else:
        speak_response("You found a treasure chest. Well done!")

# Get Input Function with Timeout
def get_input(timeout=3):
    """Wait for user input with a timeout."""
    print("Enter your input (e.g., 8, 8008135, or *): ")
    start_time = time.time()
    while time.time() - start_time < timeout:
        user_input = input("> ").strip()
        if user_input:
            return user_input
    return ""

# Main Program Loop
def main():
    while True:
        user_input = get_input()

        if user_input == "8":
            magic_8_ball()
        elif user_input in audio_clips:
            play_audio(user_input)
        elif user_input == "*":
            speak_response("Goodbye.")
            break
        else:
            speak_response("I didn't recognize that. Please try again.")

# Run the Program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak_response("Shutting down. Goodbye!")
