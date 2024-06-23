def is_valid_walk(walk):
    north_south, east_west = walk.count('n') == walk.count('s'), walk.count('e') == walk.count('w')
    length = len(walk) == 10
    return north_south and east_west and length