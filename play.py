import math
import gd
import mouse
import pickle

mem = gd.memory.get_memory()
file = input('Macro to play: ')
data = open('macros/' + file, 'rb').read()
jump_at = pickle.loads(data)

input('Please be on the main menu. Are you?')
print('The replay will start once you enter the level.')
while 1:
    while mem.is_in_level():
        print('Playing')
        for dict in jump_at:
            if dict['pos'] == mem.x_pos:
                mouse.play([dict['event']])
            
        if mem.is_dead():
            print('Restarting')
        if math.floor(mem.percent) == 100:
            print('Finished!')
            break

