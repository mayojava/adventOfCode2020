def main():
    f = open('day20.txt', 'r')

    tile_data = []
    tiles = []
    for line in f:
        if len(line.strip()) == 0:
            tiles[-1].set_data(tile_data)
            tile_data = []
            continue

        line = line.strip()
        if line.startswith('Tile'):
            line = line.split()
            id = line[1][0:-1]
            tiles.append(Tile(id))
        else:
            line = list(line)
            tile_data.append(line)
    
    tiles[-1].set_data(tile_data)

    for tile in tiles:
        find_match(tile, tiles)

    prod = 1
    for tile in tiles:
        if tile.count == 2:
            prod *= int(tile.id)
    print('prod', prod)

def find_match(tile, tiles):
    for t in tiles:
        if t.id == tile.id: continue
    
        if compare(tile.top(), t) or compare(tile.bottom(), t) or compare(tile.left(), t) or compare(tile.right(), t):
            #print(tile.id, '<---->', t.id)
            tile.increase_match_count()
            continue

def compare(layer, tile):
    if layer == tile.top(): return True
    else :
        cp = tile.top().copy()
        cp.reverse()
        if layer == cp: return True


    if layer == tile.bottom(): return True
    else:
        cp = tile.bottom()
        cp.reverse()
        if layer == cp: return True
    
    
    if layer == tile.right(): return True
    else:
        cp = tile.right()
        cp.reverse()
        if layer == cp: return True

    
    if layer == tile.left(): return True
    else:
        cp = tile.left()
        cp.reverse()
        if layer == cp: return True
    
    return False

class Tile:
    def __init__(self, id):
        self.id = id
        self.count = 0

    def set_data(self, data):
        self.data = []
        for row in data:
            n_row = []
            for col in row:
                if col == '#': n_row.append(1)
                else: n_row.append(0)
            self.data.append(n_row)

    def show_data(self):
        print(self.id)
        for row in self.data:
            print(row)
    
    def get_data(self): return self.data

    def increase_match_count(self): self.count += 1

    def top(self): return self.data[0].copy()
    def bottom(self): return self.data[-1].copy()

    def left(self):
        left = []
        for i in range(0, len(self.data)):
            left.append(self.data[i][0])
        return left

    def right(self):
        right = []
        for i in range(0, len(self.data)):
            right.append(self.data[i][-1])
        return right

if __name__ == "__main__":
    main()