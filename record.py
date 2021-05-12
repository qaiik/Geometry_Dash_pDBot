import keyboard
import pickle
import mouse
import gd

print('Ok. Enter a level to start recording')
mem = gd.memory.get_memory()

jump_at = []
def handle(event):
    jump_at.append({'pos':mem.x_pos,'event':event})

while 1:
    if mem.is_in_level():
        mouse.hook(handle)
        print('Recording')
        break

keyboard.wait('s')
mouse.unhook(handle)

file = input('What should this macro be called? ')

pickled = pickle.dumps(jump_at)

with open('macros/' + file,'wb') as f:
    f.write(pickled)

print('Saved!')
    



            
            
    
    
    
        


        
