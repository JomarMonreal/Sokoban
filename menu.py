import display_clearer
import game_file_handler

#displays the main menu screen to the terminal
def display_main_menu():
    display_clearer.clear()
    print("="*30)
    print("SOKOBAN")
    print("[1] 10x10 Mode")
    print("[2] 15x15 Mode")
    print("[0] Exit")
    user_input= int(input("Enter option: "))
    print("="*30)
    return user_input

#display the menu for any specified game mode
def display_game_mode_menu(game_mode_data):
    display_clearer.clear()
    print("="*30)
    print("SOKOBAN")
    print("High Score: " + str(game_file_handler.load_highscore(game_mode_data)) + " seconds")
    if game_file_handler.load_game(game_mode_data)!=None:
        print("[2] Continue Last Save")
    print("[1] Start New Game")
    print("[0] Back to Main Menu")
    user_input= int(input("Enter option: "))
    print("="*30)
    return user_input

#displays the options the user can take in gameplay
def display_gameplay_menu():
    print("="*30)
    print("What's your move?")
    print("[W] Up [S] Down [A] Left [D] Right")
    print("[R] Restart")
    print("[Z] Save")
    print("[X] Back to Main Menu")

