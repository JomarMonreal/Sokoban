import position_handler
import game_object_types

#check if the object is movable to the target position
def movable(game_obj,direction,target_position,game_obj_positions):
    if game_obj[0]=="P":
        is_movable=True
        for game_id in game_obj_positions:
            if game_obj_positions[game_id] == target_position:
                if game_id[0]==game_object_types.WALL:
                    return False
                elif game_id[0]==game_object_types.BOX:
                    box_position_x=game_obj_positions[game_id][0]
                    box_position_y=game_obj_positions[game_id][1]
                    box_target_position=position_handler.get_target_position(direction,box_position_x,box_position_y)
                    if movable(game_id,direction,box_target_position,game_obj_positions)==False:
                        return False

    if game_obj[0]=="B":
        is_movable=True
        for game_id in game_obj_positions:
            if game_obj_positions[game_id] == target_position:
                if game_id[0]==game_object_types.WALL or game_id[0]==game_object_types.BOX:
                    return False

    return is_movable

#move the object at a certain direction
def move(game_obj,direction,layer_map,game_obj_positions):
    game_obj_position_x=game_obj_positions[game_obj][0]
    game_obj_position_y=game_obj_positions[game_obj][1]
    target_position=position_handler.get_target_position(direction,game_obj_position_x,game_obj_position_y)
    is_movable=movable(game_obj,direction,target_position,game_obj_positions)
    
    if is_movable:
        obstruction=""
        for game_id in game_obj_positions:
            if game_obj_positions[game_id]==target_position:
                obstruction=game_id
                if obstruction[0] == game_object_types.BOX:
                    move(obstruction,direction,layer_map,game_obj_positions)
                    if game_obj_positions[obstruction]==target_position:
                        break
        else:
            layer_map[game_obj_position_y][game_obj_position_x]=" "
            layer_map[target_position[1]][target_position[0]]=game_obj[0]
            game_obj_positions[game_obj]=target_position

#move the player according to player input
def move_player(user_input,foreground_map,positions):
    direction=""
    if user_input in "Ww":
        direction="up"
    if user_input in "Ss":
        direction="down"
    if user_input in "Aa":
        direction="left"
    if user_input in "Dd":
        direction="right"
    #P0 is the player's id
    move("P0",direction,foreground_map,positions)