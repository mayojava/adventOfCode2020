import sys
from copy import deepcopy

def main():
    f = open('day24.txt', 'r')

    ref = (0,0)
    map = {ref: True}

    for line in f:
        line = line.strip()
        current = (0,0)

        index = 0
        while index < len(line):
            mv = ''
            if line[index] == 'n' or line[index] == 's':
                mv += line[index]
                index += 1
                mv += line[index]
            else: 
                mv += line[index]
            
            current = move(current, mv)

            index += 1
        
        if current in map:
            map[current] = not map[current]
        else:
            map[current] = False

    black_tiles = []
    
    count = 0
    for key in map:
        if not map[key]:
            count += 1
            black_tiles.append(key)
    
    print('total', count)
    print(black_tiles)

    do_lobby_tiles(black_tiles, 100)

def do_lobby_tiles(tiles, count):
    for i in range(0, count):
        alive_next = []

        for tile in tiles:
            neighbors = get_black_adjacent(tile, tiles)

            if neighbors == 0 or neighbors > 2: pass
            else: alive_next.append(tile)
            
            check_white(tile, tiles, alive_next)
        
        tiles = []
        for t in alive_next:
            if t not in tiles:
                tiles.append(t)

        print('Day ', i+1, len(tiles))

def check_white(tile, blacks, next):
    mv = ['e', 'se', 'sw', 'w', 'nw', 'ne']

    for d in mv:
        res = move(tile, d)
        if res not in blacks:
            n_res = get_black_adjacent(res, blacks)
            if n_res == 2:
                next.append(res)

def get_black_adjacent(tile, map):
    count = 0
    res = move(tile, 'e')
    if res in map: count += 1

    res = move(tile, 'se')
    if res in map: count += 1

    res = move(tile, 'sw')
    if res in map: count += 1

    res = move(tile, 'w')
    if res in map: count += 1

    res = move(tile, 'nw')
    if res in map: count += 1

    res = move(tile, 'ne')
    if res in map: count += 1

    return count

def move(tile, mv):
    if mv == 'e': return (tile[0]+1, tile[1])
    if mv == 'se': return (tile[0], tile[1]+1)
    if mv == 'sw': return (tile[0]-1, tile[1]+1)
    if mv == 'w': return (tile[0]-1, tile[1])
    if mv == 'nw': return (tile[0], tile[1]-1)
    if mv == 'ne': return (tile[0]+1, tile[1]-1)
    
if __name__ == '__main__':
    main()