from print_song import song_line
from time import sleep
bottle_count = 99
while bottle_count >= 0:
    print(song_line(bottle_count))
    bottle_count -= 1
    sleep(1)