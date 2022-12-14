import os
import random

#returns a random map from game_maps
def generate():
    maps=os.listdir("game_maps_10x10")
    return maps[random.randint(0,len(maps)-1)]

def randomize_order(map_list):
    result_list=[]
    while len(map_list)>0:
        result_list.append(map_list.pop(random.randint(0,len(map_list)-1)))
    return result_list