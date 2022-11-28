import game_object_types
import list_cloner

#convert map into a list of strings
def convert_to_string_list(input_map):
    map_data=[]
    for row in input_map:
        row_data=""
        for tile in row:
            row_data+=tile
        row_data+="\n"
        map_data.append(row_data)  
    return map_data

#get the foreground element of the map (PLAYER,BOX,WALL)
def get_foreground_from_default(level_map):
    foreground_layer=[]
    for row in level_map:
        foreground_row=[]
        for tile in row:
            if tile!=game_object_types.TRIGGER:
                foreground_row.append(tile)
            else:
                foreground_row.append(" ")
        foreground_layer.append(foreground_row)
    return foreground_layer

#get the foreground element of the map (TRIGGER)
def get_background_from_default(level_map):
    background_layer=[]
    for row in level_map:
        background_row=[]
        for tile in row:
            if tile==game_object_types.TRIGGER:
                background_row.append(tile)
            else:
                background_row.append(" ")
        background_layer.append(background_row)
    return background_layer

#displays/renders the map to the terminal
def display(background,foreground):
    result_map=list_cloner.clone(background)

    for i in range(len(result_map)):
        row=result_map[i]
        for j in range(len(row)):
            if foreground[i][j] == " ":
                continue
            result_map[i][j]=foreground[i][j]

    for row in result_map:
        for tile in row:
            print(tile,end="")
        print()