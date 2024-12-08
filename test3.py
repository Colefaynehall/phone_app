import time
import random
from playsound import playsound
import os

#1111tts_engine.setProperty('rate', 100)  # Set speed to 150 words per minute (default is usually ~200)

# Predefined Audio Clips with Placeholders
audio_clips = {
    "2726366": "Downloads/PhoneAudio/brandon.mp3", #brandon
    "8008135": "path/to/boobies_joke.mp3",  # Placeholder path
    "69": "Downloads/PhoneAudio/Nice.mp3",              #nice
    "420": "path/to/weed_joke.mp3",        # Placeholder path
    "911": "path/to/sirens.mp3",           # Placeholder path
    "007": "Downloads/PhoneAudio/007.mp3", #bond
    "58227": "Downloads/PhoneAudio/lucas.mp3", #lucas
    "2653": "Downloads/PhoneAudio/FILLER.mp3", #Cole
    "3326": "Downloads/PhoneAudio/FILLER.mp3", #Dean
    "42846": "Downloads/PhoneAudio/FILLER.mp3", #Gavin
    "62426": "Downloads/PhoneAudio/FILLER.mp3", #Magan
    "54372": "Downloads/PhoneAudio/FILLER.mp3", #Liesa
    "666": "Downloads/PhoneAudio/FILLER.mp3", #Mom
    "7826": "Downloads/PhoneAudio/FILLER.mp3", #Stan
    "38679": "Downloads/PhoneAudio/FILLER.mp3", #Dumpy
    "644437": "Downloads/PhoneAudio/no no no.mp3", #No no no (for bad words)
    "738273": "Downloads/PhoneAudio/no no no.mp3", #^
    "324467": "Downloads/PhoneAudio/no no no.mp3", #^^
    "528736": "Downloads/PhoneAudio/lauren copy.mp3", #Lauren
    "22532": "Downloads/PhoneAudio/FILLER.mp3", #Caleb


}

# Play Audio Function
def play_audio(clip_name):
    """Plays an audio clip."""
    if clip_name in audio_clips:
        clip = audio_clips[clip_name]
        if os.path.exists(clip):  # Check if the file exists
            print(f"Playing: {clip}")
            playsound(clip)
        else:
            print(f"Audio file not found: {clip}")  # Fallback message
    else:
        print("Invalid input.")

# Text-to-Speech Response Placeholder
def speak_response(message):
    """Simulate speaking a response (replace with actual TTS if needed)."""
    print(f"TTS: {message}")

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
        elif user_input == "2653":
            speak_response("Hello, this is Cole's message.")
        elif user_input == "1111":
            adventure_game()
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
