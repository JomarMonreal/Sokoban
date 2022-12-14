import game_map

#saves game in time,background,foreground,levels format
def save_game(background,foreground,time_spent,levels_remaining,data_folder):
    #initialization
    time_spent_data=str(time_spent)
    background_data=game_map.convert_to_string_list(background)
    foreground_data=game_map.convert_to_string_list(foreground)
    
    #writing data to file
    game_data_file=open(data_folder+"/time_spent.txt","w")
    game_data_file.write(time_spent_data)
    game_data_file.close()

    game_data_file=open(data_folder+"/background.txt","w")
    game_data_file.writelines(background_data)
    game_data_file.close()

    game_data_file=open(data_folder+"/foreground.txt","w")
    game_data_file.writelines(foreground_data)
    game_data_file.close()

    game_data_file=open(data_folder+"/levels_remaining.txt","w")
    for level in levels_remaining:
        game_data_file.write(level+"\n")
    game_data_file.close()

    print("="*30)
    print("Saved Game!")
    return True

def save_highscore(highscore,data_folder):
    file_handler=open(data_folder+"/highscore.txt","w")
    file_handler.write(str(highscore))
    file_handler.close()

def load_highscore(data_folder):
    try:
        file_reader=open(data_folder+"/highscore.txt","r")
        highscore=float(file_reader.read())
        file_reader.close()
        return highscore
    except:
        return 0

def load_game(data_folder):
    try:
        #initialization
        background_data=[]
        foreground_data=[]
        remaining_levels=[]
        time_spent=0

        #reading file
        game_data_file=open(data_folder+"/time_spent.txt","r")
        time_spent=float(game_data_file.read())
        game_data_file.close()

        game_data_file=open(data_folder+"/levels_remaining.txt","r")
        game_data_lines=game_data_file.readlines()
        for line in game_data_lines:
            line=line[:-1]
            remaining_levels.append(line)
        game_data_file.close()

        game_data_file=open(data_folder+"/background.txt","r")
        game_data_lines=game_data_file.readlines()
        for line in game_data_lines:
            line=line[:-1]
            background_data.append([char for char in line])
        game_data_file.close()

        game_data_file=open(data_folder+"/foreground.txt","r")
        game_data_lines=game_data_file.readlines()
        for line in game_data_lines:
            line=line[:-1]
            foreground_data.append([char for char in line])
        game_data_file.close()

        return time_spent,remaining_levels,background_data,foreground_data
    except:
        return None


#load map from game_maps (default)
def load_default_level_map(maps_folder,level):
    level_map_file=open(maps_folder+"/"+level,"r")
    level_map_rows=level_map_file.readlines()
    level_map=[]
    for row in level_map_rows:
        row=row.replace("\n","")
        level_map.append([tile for tile in row])
    return level_map

if __name__=='__main__':
    print(load_highscore("highscore_10x10.txt","game_mode_10x10_data"))