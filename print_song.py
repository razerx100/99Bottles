"""function for song printing"""
def song_line(bottles):
    """ prints song """
    beer_on_wall = bottles - 1
    if bottles >= 2:
        return ("{0} bottles of beer on the wall, {0} bottles of beer.".format(bottles)
                + "\nTake one down and"
                + " pass it around, {0} bottles of beer on the wall.\n".format(beer_on_wall))
    if bottles == 1:
        return ("{0} bottle of beer on the wall, {0} bottles of beer.".format(bottles)
                + "\nTake one down and "
                + "pass it around, no more bottles of beer on the wall.\n")
    if bottles == 0:
        return ("No more bottles of beer on the wall, no more bottles of beer."
                + "\nGo to the store "
                + "and buy some more, 99 bottles of beer on the wall.")
    return ""
