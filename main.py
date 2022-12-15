"""
Jomar P. Monreal
CMSC 12 T23L
This is a simple Sokoban game that can be played at the terminal.
"""
import menu
import gameplay


#main program for SOKOBAN
def main():
    #initialization
    has_saved=False
    has_continued=False
    highscore=0

    #main program loop
    user_input=-1
    while user_input !=0:
        user_input=menu.display_main_menu()

        #if chosen 10x10 mode
        if user_input==1:
            user_game_mode_input=menu.display_game_mode_menu("game_mode_10x10_data")
            #if want to start a new game
            if user_game_mode_input==1:
                gameplay.start("game_maps_10x10","game_mode_10x10_data",False)
            #if want to continue last save
            elif user_game_mode_input==2:
                gameplay.start("game_maps_10x10","game_mode_10x10_data",True)
        
        #if chosen 15x15 mode
        elif user_input==2:
            user_game_mode_input=menu.display_game_mode_menu("game_mode_15x15_data")
            #if want to start a new game 
            if user_game_mode_input==1:
                gameplay.start("game_maps_15x15","game_mode_15x15_data",False)
            #if want to continue last save
            elif user_game_mode_input==2:
                gameplay.start("game_maps_15x15","game_mode_15x15_data",True)
            
        #wants to exit
        else:
            print("Thank you for playing!")
            user_input=0
                

if __name__=="__main__":
    main()