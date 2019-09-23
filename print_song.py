def song_line(bottles):
    # prints song
    beer_on_wall = bottles - 1
    if bottles >= 2:
        return "{0} bottles of beer on the wall, {1} bottles of beer.\nTake one down and pass it around, {2} bottles of beer on the wall.\n".format(bottles, bottles, beer_on_wall)
    elif bottles == 1:
        return "{0} bottle of beer on the wall, {1} bottles of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n".format(bottles, bottles)
    elif bottles == 0:
        return "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.".format(bottles, bottles)