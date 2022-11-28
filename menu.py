#displays the main menu screen to the terminal
def display_main_menu(has_saved,highscore):
    print("="*30)
    print("SOKOBAN")
    print("High Score: " + str(highscore) + " seconds")
    if has_saved:
        print("[1] Continue Last Save")
        print("[2] Start New Game")
    else:
        print("[1] Start New Game")
    print("[0] Exit")
    user_input= int(input("Enter option: "))
    print("="*30)
    return user_input

#displays the options the user can take in gameplay
def display_game_menu():
    print("="*30)
    print("What's your move?")
    print("[W] Up [S] Down [A] Left [D]Right")
    print("[R] Restart")
    print("[Z] Save")
    print("[X] Back to Main Menu")

