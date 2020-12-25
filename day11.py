def main():
    f  = open('day11.txt', 'r')
    seats = []
    for line in f:
        line = line.strip()
        seats.append(list(line))

    copy = []
    for l in seats:
        copy.append(l.copy())

    #index = 0

    while True:
        for row in range(0, len(seats)):
            for col in range(0, len(seats[0])):

                if seats[row][col] == '.':
                    continue
                if seats[row][col] == 'L':
                    no_occu = no_occupied_seat(seats, row, col)
                    if no_occu:
                        copy[row][col] = '#'
                elif seats[row][col] == '#':
                    f_or = four_or_more_occupied(seats, row, col)
                    if f_or:
                        copy[row][col] = 'L'
                else:
                    print('non conformist')
        
        res = do_copy_over(seats, copy)
        if not res:
            print(count_occupied(seats))
            break
        
        #index+=1

def count_occupied(seats):
    count = 0
    for row in range(0, len(seats)):
        for col in range(0, len(seats[0])):
            if seats[row][col] == '#':
                count+= 1
    return count 

def do_copy_over(real, copy):
    res = False
    for row in range(0, len(real)):
        for col in range(0, len(real[0])):
            if real[row][col] != copy[row][col]:
                res = True
                real[row][col] = copy[row][col]
    return res

def no_occupied_seat(seats, row, col):
    directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,1), (-1,-1), (1,1), (1,-1)]

    for d in directions:
        nr = row+d[0]
        nc = col+d[1]

        if nr >= 0 and nr < len(seats) and nc >= 0 and nc < len(seats[0]):
            seat = seats[nr][nc]

            if seat == '#':
                return False
    return True

def four_or_more_occupied(seats, row, col):
    count = 0
    directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,1), (-1,-1), (1,1), (1,-1)]

    for d in directions:
        nr = row+d[0]
        nc = col+d[1]

        if nr >= 0 and nr < len(seats) and nc >= 0 and nc < len(seats[0]):
            seat = seats[nr][nc]

            if seat == '#':
                count += 1

    return count >= 4

if __name__ == '__main__':
    main()
