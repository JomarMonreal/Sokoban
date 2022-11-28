import time
import game_object_types

#check if the user finished the game
def has_finished_game(positions):
    #initialization
    box_positions=[]
    trigger_positions=[]

    #get the position of all boxes and triggers
    for game_id in positions:
        if game_id[0]==game_object_types.BOX:
            box_positions.append(positions[game_id])
        elif game_id[0]==game_object_types.TRIGGER:
            trigger_positions.append(positions[game_id])
    
    #check if all boxes are in the trigger positions
    is_finished=True
    for trigger_position in trigger_positions:
        has_box=False
        for box_position in box_positions:
            if trigger_position==box_position:
                has_box=True
                break
        if has_box==False:
            is_finished=False
            break
    
    return is_finished

#finishes the game
def finish_game(start_time,saved_time_spent,highscore):
    #intialization
    has_saved=False
    has_continued=False
    
    #computes the score and save as new highscore when beaten previous record
    end_time=time.time()
    time_spent=round((end_time-start_time)+saved_time_spent,2)
    if highscore==0 or time_spent<highscore:
        highscore=time_spent
    
    print("You have solved the puzzle for " + str(time_spent) +" seconds.")
    return has_saved,has_continued,highscore