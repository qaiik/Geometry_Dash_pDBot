import pickle

while 1:
    cmd = input('pD$ ')
    if cmd == 'play':
        import play
    if cmd == 'save':
        import record
    if cmd != 'save' and cmd != 'play':
        print('pD : UNKOWN COMMAND')
        
