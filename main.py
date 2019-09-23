"""time flies"""
from time import sleep
from print_song import song_line
BOTTLE_COUNT = 99
while BOTTLE_COUNT >= 0:
    print(song_line(BOTTLE_COUNT))
    BOTTLE_COUNT -= 1
    sleep(1)
