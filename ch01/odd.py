from datetime import datetime
from os import getcwd
from random import randint
from time import sleep

odds = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

where_am_i = getcwd()

for i in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This minute seems a little odd. But at least I'm here: " + where_am_i + "_")
    else:
        print("Not an odd minute. But at least I'm here: " + where_am_i)
    wait_time = randint(1,20)
    print(wait_time)
    sleep(wait_time)
