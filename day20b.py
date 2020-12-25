import math

def main():
    f = open('day20.txt', 'r')

    tile_data = []
    tiles = []
    tiles_count = 0

    for line in f:
        if len(line.strip()) == 0:
            tiles[-1].set_data(tile_data)
            tile_data = []
            tiles_count+=1
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
    tiles_count += 1

    print('there are', tiles_count, 'tiles')

    for tile in tiles: #builds the connection of mathcing sides
        find_match(tile, tiles)
    
    adj = build_adjacency(tiles)
    
    source = ''
    corners = []
    
    for tile in tiles:
        if tile.count == 2:
            if source == '':
                source = tile.id
            corners.append(tile.id)
    

    pred = {}
    dist = {}
    bfs(adj, source, pred, dist, [])

    #print(corners)
    corner_paths = []
    cc_corners = corners.copy()
    
    for key in dist:
        if dist[key] == int(math.sqrt(tiles_count) - 1) and key in cc_corners:
            partials = [source]
            partials += get_path(source, key, pred)
            corner_paths.append(partials)
            cc_corners.remove(key)
    
    cc_corners.remove(source)
    
    pred = {}
    dist = {}
    bfs(adj, cc_corners[0], pred, dist, [])
    for key in dist:
        if dist[key] == int(math.sqrt(tiles_count)) - 1 and key in corners:
            partials = [cc_corners[0]]
            partials += get_path(cc_corners[0], key, pred)
            corner_paths.append(partials)
    
    grid = [['f' for j in range(0, int(math.sqrt(tiles_count)))] for i in range(0, int(math.sqrt(tiles_count)))]
    grid[0] = corner_paths[0]
    corner_paths[2].reverse()
    grid[len(grid)-1] = corner_paths[2]

    #pick second
    pick_second(grid, corner_paths[1])
    #pick last
    pick_last(grid, corner_paths[3])
    
    
    fill_up(grid, adj)
    for r in grid:
        print(r)
    print()
    for h in tiles:
        print(h.id, h.side)

    arranged = [[] for r in grid]
    for row in range(0, len(arranged)):
        items_in_row = grid[[row]]
        i,j = 0,1

        while i < len(items_in_row) and j < len(items_in_row):
            tile_i = find_tile_with_id(tiles, i)
            tile_j = find_tile_with_id(tiles, j)

            data_i = tile_i.data
            data_j = tile_j.data

            matching_sides = find_matching_side(tile_i, tile_j)

            res1 = turn(tile_i, matching_sides[0])
            res2 = turn(tile_j, matching_sides[1])

            if len(arranged[row]) == 0:
                arranged[row].append([res1, res2])
            else:

            i = j
            j += 1


def find_matching_side(tile1, tile2):
    for idx,val in enumerate(tile1.side):
        for idx2,val2 in enumerate(tile2.side):
            if val == val2 or val == val2.copy()[::-1]:
                return (idx, idx2)
    return None

def find_tile_with_id(tiles, id):
    for tile in tiles:
        if tile.id == id:
            return tile
    return None

def rotate_left(tile):
    rotataed = []
    for i in range(-1, -(len(tile)+1), -1):
        row = []
        for j in range(0, len(tile)):
            row.append(tile[j][i])
        rotataed.append(row)
    return rotataed

def rotate_right(tile):
    rotated = []
    for i in range(0, len(tile)):
        row = []
        for j in range(0, len(tile)):
            row.append(tile[j][i])
        rotated.append(row[::-1])

def flip(tile):
    return tile[::-1]


def fix_orientation(grid, tiles):
    pass

def fill_up(grid, adj):
    for index in range(1, len(grid)-1):
        start = grid[0][index]
        end = grid[len(grid)-1][index]

        pred = {}
        dist = {}
        bfs(adj, start, pred, dist, [])

        path = get_path(start, end, pred)
        path.pop(-1)

        row_index = 1
        for p in path:
            grid[row_index][index] = p
            row_index += 1

def pick_last(grid, cp):
    cp.reverse()
    cp.pop(0)
    cp.pop(-1)

    row = 1
    for p in cp:
        grid[row][-1] = p
        row += 1

def pick_second(grid, cp):
    cp.pop(0)
    cp.pop(-1)

    row = 1
    for p in cp:
        grid[row][0] = p
        row += 1
    

def get_path(source, dest, pred):
    path = [dest]
    while True:
        along = pred[dest]
        if along == source: break
        path.insert(0, along)
        dest = along
    return path

def build_adjacency(tiles):
    map = {}

    for tile in tiles:
        map[tile.id] = []
        for t in tile.aligns.keys():
            map[tile.id].append(t)
    
    return map

def bfs(adj, source, pred, dist, visited):
    queue = [source]
    dist[source] = 0
    visited.append(source)

    while len(queue) > 0:
        current = queue.pop(0)
        for con in adj[current]:
            if con not in visited:
                visited.append(con)
                queue.append(con)
                pred[con] = current
                dist[con] = dist[current] + 1


def find_match(tile, tiles):
    for t in tiles:
        if t.id == tile.id: continue

        side = compare(tile.top(), t)
        if side:
            tile.set_aligns(1, side, t.id)
            tile.increase_match_count()
            continue
        
        side = compare(tile.right(), t)
        if side:
            tile.set_aligns(2, side, t.id)
            tile.increase_match_count()
            continue
        
        side = compare(tile.bottom(), t)
        if side:
            tile.set_aligns(3, side, t.id)
            tile.increase_match_count()
            continue
        
        side = compare(tile.left(), t)
        if side:
            tile.set_aligns(4, side, t.id)
            tile.increase_match_count()
            continue

        #if compare(tile.top(), t) or compare(tile.bottom(), t) or compare(tile.left(), t) or compare(tile.right(), t):
            #print(tile.id, '<---->', t.id)
         #   tile.increase_match_count()
          #  continue

def compare(layer, tile):
    if layer == tile.top(): return 1
    else :
        cp = tile.top().copy()
        cp.reverse()
        if layer == cp: return -1


    if layer == tile.bottom(): return 3
    else:
        cp = tile.bottom()
        cp.reverse()
        if layer == cp: return -3
    
    
    if layer == tile.right(): return 2
    else:
        cp = tile.right()
        cp.reverse()
        if layer == cp: return -2

    
    if layer == tile.left(): return 4
    else:
        cp = tile.left()
        cp.reverse()
        if layer == cp: return -4
    
    return None

class Tile:
    def __init__(self, id):
        self.id = id
        self.count = 0
        self.aligns = {}
        self.side = []

    def set_data(self, data):
        self.data = []
        for row in data:
            n_row = []
            for col in row:
                if col == '#': n_row.append(1)
                else: n_row.append(0)
            self.data.append(n_row)
        self.compute_sides()

    def compute_sides(self):
        top = self.data[0].copy()
        top = [str(x) for x in top]
        top = ''.join(top)
        self.side.append((int(top,2), int(top[::-1], 2)))
        
        right = []
        for i in range(0, len(self.data)):
            right.append(str(self.data[i][-1]))
        right = ''.join(right)
        self.side.append((int(right,2), int(right[::-1],2)))

        bottom = self.data[-1].copy()
        bottom = [str(x) for x in bottom]
        bottom = ''.join(bottom)
        self.side.append((int(bottom,2), int(bottom[::-1],2)))

        left = []
        for i in range(0, len(self.data)):
            left.append(str(self.data[i][0]))
        left = ''.join(left)
        self.side.append((int(left,2), int(left[::-1],2)))
        

    def show_data(self):
        print(self.id)
        for row in self.data:
            print(row)
    
    def get_data(self): return self.data

    def increase_match_count(self): self.count += 1

    def set_aligns(self, myside, yourside, id):
        self.aligns[id] = (myside, yourside)

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