import os
import random

#returns a random map from game_maps
def generate():
    maps=os.listdir("game_maps")
    return maps[random.randint(0,len(maps)-1)]