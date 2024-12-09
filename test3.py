import time
import random
from playsound import playsound
import os
import pyttsx3

# Initialize TTS engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 130)  # Slower speed
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[12].id)  # Use the first voice

# Text-to-Speech Response
def speak_response(message):
    """Speak a text response using TTS."""
    print(f"TTS: {message}")
    tts_engine.say(message)
    tts_engine.runAndWait()

# Predefined Audio Clips with Placeholders
audio_clips = {
    "2726366": "PhoneAudio/brandon.mp3", #brandon
    "69": "PhoneAudio/Nice.mp3",              #nice
    "420": "path/to/weed_joke.mp3",        # Placeholder path
    "911": "path/to/sirens.mp3",           # Placeholder path
    "007": "PhoneAudio/007.mp3", #bond
    "58227": "PhoneAudio/lucas.mp3", #lucas
    "2653": "PhoneAudio/FILLER.mp3", #Cole
    "3326": "PhoneAudio/FILLER.mp3", #Dean
    "42846": "PhoneAudio/FILLER.mp3", #Gavin
    "62426": "PhoneAudio/FILLER.mp3", #Magan
    "54372": "PhoneAudio/FILLER.mp3", #Liesa
    "666": "PhoneAudio/FILLER.mp3", #Mom
    "7826": "PhoneAudio/FILLER.mp3", #Stan
    "38679": "PhoneAudio/FILLER.mp3", #Dumpy
    "644437": "PhoneAudio/no no no.mp3", #No no no (for bad words)
    "738273": "PhoneAudio/no no no.mp3", #^
    "324467": "PhoneAudio/no no no.mp3", #^^
    "528736": "PhoneAudio/lauren copy.mp3", #Lauren
    "22532": "PhoneAudio/FILLER.mp3", #Caleb


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

# Dice Roll
def roll_dice(sides=6):
    speak_response(f"Rolling a {sides}-sided die...")
    speak_response(f"You rolled a {random.randint(1, sides)}!")

    
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

# Blackjack Functionality
def blackjack():
    def calculate_hand_value(hand):
        """Calculate the total value of a hand."""
        value = 0
        aces = 0
        for card in hand:
            if card in ['Jack', 'Queen', 'King']:
                value += 10
            elif card == 'Ace':
                value += 11
                aces += 1
            else:
                value += card
        
        # Adjust for aces if total exceeds 21
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        
        return value

    def deal_card():
        """Deal a random card."""
        return random.choice(['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'])

    # Initialize hands
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    speak_response(f"Your hand: {player_hand}")
    speak_response(f"Dealer's hand: [{dealer_hand[0]}, ?]")


    # Player's turn
    while True:
        player_value = calculate_hand_value(player_hand)
        speak_response(f"Your total: {player_value}")
        

        if player_value > 21:
            speak_response("You busted! Buster. MWAHAHAHA.")
            return

        choice = input("Enter 1 to hit or 2 to stand: ").strip().upper()
        if choice == "1":
            new_card = deal_card()
            player_hand.append(new_card)
            speak_response(f"You drew: {new_card}")
        elif choice == "2":
            break
        else:
            speak_response("Invalid input, please enter 1 or 2.")

    # Dealer's turn
    speak_response(f"Dealer's hand: {dealer_hand}")
    while calculate_hand_value(dealer_hand) < 17:
        new_card = deal_card()
        dealer_hand.append(new_card)
        speak_response(f"Dealer drew: {new_card}")

    dealer_value = calculate_hand_value(dealer_hand)
    player_value = calculate_hand_value(player_hand)
    speak_response(f"Your total: {player_value}")
    speak_response(f"Dealer's total: {dealer_value}")

    # Determine the winner
    if dealer_value > 21 or player_value > dealer_value:
        speak_response("You win! Congratulations, nerd")
    elif player_value < dealer_value:
        speak_response("Dealer wins! Which means you lose. haha. bitch")
    else:
        speak_response("It's a tie! Which is basically losing. loser.")

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
        elif user_input == "777":
            roll_dice()
        elif user_input == "21":
            speak_response(f"Welcome to Blackjack. Enter 1 to hit or 2 to stand: ")
            blackjack()
        elif user_input == "4357":
           speak_response("HELP. PLEASE GOD HELP. IT BURNS. EVERYTHING IS DARK. LET ME OUT. LET ME OUT. LET MEEEEEEEEE OUTTTTT.")   
        elif user_input == "8008135":
            speak_response("hahahaha hehehe. boobies. ha.")
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
