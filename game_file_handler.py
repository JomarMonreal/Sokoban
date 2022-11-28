import game_map

#saves game in time,background,foreground format
def save_game(level,background,foreground,time_spent):
    #initialization
    time_spent_data=[str(time_spent)+"\n"]
    background_data=["Background:\n"]+game_map.convert_to_string_list(background)
    foreground_data=["Foreground:\n"]+game_map.convert_to_string_list(foreground)
    
    #writing data to file
    filename=level[:-4]+"_data.txt"
    game_data_file=open("game_maps_data/"+filename,"w")
    game_data_file.writelines(time_spent_data)
    game_data_file.writelines(background_data)
    game_data_file.writelines(foreground_data)

    #closing file
    game_data_file.close()
    print("="*30)
    print("Saved Game!")
    return True

#loads game retieving time, background and foreground
def load_game(level):
    #initialization
    is_background=True
    got_time=False
    time_spent=0
    background_data=[]
    foreground_data=[]

    #reading file
    filename=level[:-4]+"_data.txt"
    game_data_file=open("game_maps_data/"+filename,"r")
    game_data_lines=game_data_file.readlines()
    
    #extracting data from file
    for line in game_data_lines:
        game_data_line=line.replace("\n","")
        
        #get time_spent
        if got_time==False:
            time_spent=float(game_data_line)
            got_time=True
            continue

        #get foreground and background data
        if game_data_line=="Foreground:":
            is_background=False
            continue
        if is_background==False:
            if game_data_line=="Foreground:":
                continue
            foreground_data.append([char for char in game_data_line])
        else:
            if game_data_line=="Background:":
                continue
            background_data.append([char for char in game_data_line])

    return time_spent,background_data,foreground_data

#load map from game_maps (default)
def load_default_level_map(level):
    level_map_file=open("game_maps/"+level,"r")
    level_map_rows=level_map_file.readlines()
    level_map=[]
    for row in level_map_rows:
        row=row.replace("\n","")
        level_map.append([tile for tile in row])
    return level_map

if __name__=='__main__':
    print(load_game("level1.txt"))