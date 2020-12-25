def main():
    f = open('day17.txt', 'r')

    board = []
    for line in f:
        line = line.strip()
        line = list(line)
        board.append(line)
    
    #print(board)
    active_coordinates = []

    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] == '#':
                active_coordinates.append([row, col, 0, 0])
    

    for i in range(0,6):
        next_coordinates = []
        for point in active_coordinates:
            num_of_neighbors = get_neighbors_count(active_coordinates, point)

            if num_of_neighbors == 2 or num_of_neighbors == 3:
                next_coordinates.append(point)
            
            for x in range(-1, 2):
                for y in range(-1, 2):
                    for z in range(-1, 2):
                        for w in range(-1, 2):
                            if x == 0 and y == 0 and z == 0 and w == 0:
                                continue
                            new_coordinate = [point[0]+x, point[1]+y, point[2]+z, point[3]+w]

                            if new_coordinate not in active_coordinates:
                                count_n = get_neighbors_count(active_coordinates, new_coordinate)
                                if count_n == 3:
                                    next_coordinates.append(new_coordinate)
        active_coordinates = []
        for x in next_coordinates:
            if x not in active_coordinates:
                active_coordinates.append(x)
                
        print("done ", i, len(active_coordinates))
    
    print('res', len(active_coordinates))



def get_neighbors_count(board, point):
    count = 0
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for w in range(-1,2):
                    if x == 0 and y == 0 and z == 0 and w == 0:
                        continue
                    neighbor = [point[0]+x, point[1]+y, point[2]+z, point[3]+w]

                    if neighbor in board:
                        count += 1

    return count

if __name__ == '__main__':
    main()