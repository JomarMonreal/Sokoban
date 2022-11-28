import game_object_types

def get_positions(game_obj_type,level_map):
    positions={}
    count=0
    for y in range(len(level_map)):
        row=level_map[y]
        for x in range(len(row)):
            tile=row[x]
            if tile == game_obj_type:
                position=[x,y]
                game_obj_id=game_obj_type+str(count)
                positions[game_obj_id]=position
                count+=1
    return positions

def get_all_positions(background_map,foreground_map):
    positions={}
    for game_obj_type in game_object_types.GAME_OBJECT_TYPES:
        positions.update(get_positions(game_obj_type,background_map))
        positions.update(get_positions(game_obj_type,foreground_map))
    return positions

def get_target_position(direction,game_obj_position_x,game_obj_position_y):
    target_position=[]
    if direction == "up":
        target_position=[game_obj_position_x,game_obj_position_y-1]
    if direction == "down":
        target_position=[game_obj_position_x,game_obj_position_y+1]
    if direction == "left":
        target_position=[game_obj_position_x-1,game_obj_position_y]
    if direction == "right":
        target_position=[game_obj_position_x+1,game_obj_position_y]
    return target_position
