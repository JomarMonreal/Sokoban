import time
import menu
import game_file_handler
import game_map
import position_handler
import movement_handler
import game_finish_handler
import game_resetter
import map_randomizer

def start(has_continued,has_saved,highscore):
    #initialization of variables
    start_time=time.time()
    saved_time_spent=0
    level=map_randomizer.generate()
    level_map=game_file_handler.load_default_level_map(level)
    background_map=game_map.get_background_from_default(level_map)
    foreground_map=game_map.get_foreground_from_default(level_map)
    if has_continued:
        saved_time_spent,background_map,foreground_map=game_file_handler.load_game(level)
    positions=position_handler.get_all_positions(background_map,foreground_map)

    #start of game loop
    is_finished=False
    while is_finished == False:
        #check if the user completed the game
        if game_finish_handler.has_finished_game(positions):
            return game_finish_handler.finish_game(start_time,saved_time_spent,highscore)

        #displays the map and options
        game_map.display(background_map,foreground_map)
        menu.display_game_menu()
        
        #ask user to choose from the options
        user_input=" "
        while user_input not in "WwAaSsDdRrZzXx":
            user_input=input("Enter move: ")
            #move the player
            if user_input in "WwAaSsDd":
                movement_handler.move_player(user_input,foreground_map,positions)
            #resets game
            elif user_input in "Rr":
                background_map,foreground_map,positions,start_time=game_resetter.reset(level_map)
            #saves the game
            elif user_input in "Zz":
                end_time=time.time()
                time_spent=round(end_time-start_time,2)
                has_saved=game_file_handler.save_game(level,background_map,foreground_map,time_spent)
            #exits back to main menu
            elif user_input in "Xx":
                is_finished=True
            print("="*30)


    return has_continued,has_saved,highscore
