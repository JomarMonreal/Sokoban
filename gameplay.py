import os
import time
import menu
import display_clearer
import game_file_handler
import game_map
import position_handler
import movement_handler
import game_finish_handler
import game_resetter
import map_randomizer

def start(maps_folder,maps_data_folder,has_continued):
    #initialization of variables
    start_time=time.time()
    saved_time_spent=0
    levels_finished=0
    levels=[]
    if has_continued:
        saved_time_spent,levels,background_map,foreground_map=game_file_handler.load_game(maps_data_folder)
    else:
        levels=map_randomizer.randomize_order(os.listdir(maps_folder))

    is_leaving=False
    for level in levels:
        level_map=game_file_handler.load_default_level_map(maps_folder,level)
        if not has_continued:
            background_map=game_map.get_background_from_default(level_map)
            foreground_map=game_map.get_foreground_from_default(level_map)
        positions=position_handler.get_all_positions(background_map,foreground_map)

        #start of game loop
        has_finished_level=False
        while not has_finished_level:
            #displays the map and options
            display_clearer.clear()
            game_map.display(background_map,foreground_map)
            menu.display_gameplay_menu()
            
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
                    levels_remaining=levels[levels_finished:]
                    game_file_handler.save_game(background_map,foreground_map,time_spent,levels_remaining,maps_data_folder)
                #exits back to main menu
                elif user_input in "Xx":
                    has_finished_level=True
                    is_leaving=True
                print("="*30)
            
            #check if the user completed the level
            if game_finish_handler.has_finished_level(positions):
                levels_finished+=1
                has_continued=False
                has_finished_level=True

        #check if the user wants to leave
        if is_leaving:
            break

    # this is a for-else loop, the loop will only break when the user wants to
    # go back to main menu
    else:
        game_finish_handler.finish_game(start_time,saved_time_spent,maps_data_folder)

if __name__=="__main__":
    start("game_maps_15x15","game_mode_15x15_data",False)