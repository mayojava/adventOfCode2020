import sys

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
            print('seen before')
            map[current] = not map[current]
        else:
            map[current] = False
    
    count = 0
    for key in map:
        if not map[key]:
            count += 1
    
    print('total', count)
    print(map)

def get_black_adjacent(tile, map):
    count = 0
    res = move(tile.copy(), 'e')
    if res in map and not map[res]: count += 1

    res = move(tile.copy(), 'se')
    if res in map and not map[res]: count += 1

    res = move(tile.copy(), 'sw')
    if res in map and not map[res]: count += 1

    res = move(tile.copy(), 'w')
    if res in map and not map[res]: count += 1

    res = move(tile.copy, 'nw')
    if res in map and not map[res]: count += 1

    res = move(tile.copy, 'ne')
    if res in map and not map[res]: count += 1

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