import random 

def play_round(possible_hands, player_hand, computer_picks, stats): 
    computer_hand = possible_hands[random.randrange(0, 4)]
    computer_picks[computer_hand] = computer_picks[computer_hand] + 1
    print("Computer plays: " + computer_hand)
    if player_hand == "rock" and computer_hand == "rock" or player_hand == "paper" and computer_hand == "paper" or player_hand == "scissors" and computer_hand == "scissors" or player_hand == "lizard" and computer_hand == "lizard"or player_hand == "spock" and computer_hand == "spock":
        print("TIE")
        stats["tie"] = stats["tie"] + 1
    elif player_hand == "scissors" and computer_hand == "paper" or player_hand == "paper" and computer_hand == "rock" or player_hand == "rock" and computer_hand == "lizard" or player_hand == "lizard" and computer_hand == "spock" or player_hand == "spock" and computer_hand == "scissors" or player_hand == "scissors" and computer_hand == "lizard" or player_hand == "lizard" and computer_hand == "paper" or player_hand == "paper" and computer_hand == "spock" or player_hand == "spock" and computer_hand == "rock" or player_hand == "rock" and computer_hand == "scissors":
        print("WIN")
        stats["loss"] = stats["loss"] + 1
    else:
        print("LOSS")
        stats["win"] = stats["win"] + 1
    return computer_picks, stats  

def load_stats(file_path):
    try:
        file = open(file_path, "r")
        computer_picks, stats = file.split("\n")
    except FileNotFoundError:
        print("File Error")
    return computer_picks, stats

def save_stats(file_path, computer_picks, stats):
    try:
        file = open(file_path, "w")
        file.write(computer_picks + "\n" + stats)
    except FileNotFoundError:
        print("File Error")

if __name__ == "__main__":
    file_path = '20240118_stats.txt'
    #computer_picks, stats = load_stats(file_path)
    computer_picks = {"rock": 0, "paper": 0, "scissors": 0, "lizard": 0, "spock": 0}
    stats = {"tie": 0, "win": 0, "loss": 0}
    
    modus = input("Play (p) or Stats (s): ").strip()
    if modus == 'p':
        play_on = True
        possible_hands = ["rock", "paper", "scissors", "lizard", "spock"]
        while play_on: 
            player_hand = input('Choose ["rock", "paper", "scissors", "lizard", "spock"]: ').strip().lower()
            if player_hand in possible_hands:
                computer_picks, stats = play_round(possible_hands, player_hand, computer_picks, stats)
            else:
                print("Wrong Entry")
            play_on_entry = input('Play on? (y, n)')
            if play_on_entry == 'n':
                play_on = False
            elif play_on_entry != 'y':
                print("Wrong Entry")
                play_on = False
    elif modus == 's':
        print("Computer Picks: ")
        print(computer_picks)
        print("Stats: ")
        print(stats)
    else:
        print("Wrong Entry")

    #save_stats(file_path, computer_picks, stats)