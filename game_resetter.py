import time
import game_map
import position_handler

#reset to the default state of map
def reset(level_map):
    background_map=game_map.get_background_from_default(level_map)
    foreground_map=game_map.get_foreground_from_default(level_map)
    positions=position_handler.get_all_positions(background_map,foreground_map)
    start_time=time.time()
    return background_map,foreground_map,positions,start_time