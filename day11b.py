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
                    f_or = five_or_more_occupied(seats, row, col)
                    if f_or:
                        copy[row][col] = 'L'
                else:
                    print('non conformist')
        
        res = do_copy_over(seats, copy)
        #for lin in seats:
         #   print (lin)
        #print('\n\n')

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
    res = check_up(seats, row, col)
    if res == '#':
        return False
    
    res = check_down(seats, row, col)
    if res == '#':
        return False
    
    res = check_left(seats, row, col)
    if res == '#':
        return False
    
    res = check_right(seats, row, col)
    if res == '#':
        return False

    res = check_up_left(seats, row, col)
    if res == '#':
        return False

    res = check_up_right(seats, row, col)
    if res == '#':
        return False
    
    res = check_bottom_left(seats, row, col)
    if res == '#':
        return False
    
    res = check_bottom_right(seats, row, col)
    if res == '#':
        return False

    return True

def check_up(seats, row, col):
    nr = row-1
    nc = col

    while nr >= 0 and nr < len(seats) and nc >= 0 and nc < len(seats[0]):
        if seats[nr][nc] == '#':
            return '#'
        elif seats[nr][nc] == 'L':
            return 'L'
        nr -= 1
    return '.'

def check_down(seats, row, col):
    nr = row+1
    nc = col

    while nr >= 0 and nr < len(seats) and nc >= 0 and nc < len(seats[0]):
        if seats[nr][nc] == '#':
            return '#'
        elif seats[nr][nc] == 'L':
            return 'L'
        nr += 1
    return '.'

def check_left(seats, row, col):
    nr = row
    nc = col-1

    while nr >= 0 and nr < len(seats) and nc >= 0 and nc < len(seats[0]):
        if seats[nr][nc] == '#':
            return '#'
        elif seats[nr][nc] == 'L':
            return 'L'
        nc -= 1
    return '.'

def check_right(seats, row, col):
    nr = row
    nc = col+1

    while nr >= 0 and nr < len(seats) and nc >= 0 and nc < len(seats[0]):
        if seats[nr][nc] == '#':
            return '#'
        elif seats[nr][nc] == 'L':
            return 'L'
        nc += 1
    return '.'

def check_up_left(seats, row, col):
    nr = row-1
    nc = col-1

    while nr >= 0 and nr < len(seats) and nc >= 0 and nc < len(seats[0]):
        if seats[nr][nc] == '#':
            return '#'
        elif seats[nr][nc] == 'L':
            return 'L'
        nr -= 1
        nc -= 1
    return '.'

def check_up_right(seats, row, col):
    nr = row-1
    nc = col+1

    while nr >= 0 and nr < len(seats) and nc >= 0 and nc < len(seats[0]):
        if seats[nr][nc] == '#':
            return '#'
        elif seats[nr][nc] == 'L':
            return 'L'
        nr -= 1
        nc += 1
    return '.'

def check_bottom_right(seats, row, col):
    nr = row+1
    nc = col+1

    while nr >= 0 and nr < len(seats) and nc >= 0 and nc < len(seats[0]):
        if seats[nr][nc] == '#':
            return '#'
        elif seats[nr][nc] == 'L':
            return 'L'
        nr += 1
        nc += 1
    return '.'

def check_bottom_left(seats, row, col):
    nr = row+1
    nc = col-1

    while nr >= 0 and nr < len(seats) and nc >= 0 and nc < len(seats[0]):
        if seats[nr][nc] == '#':
            return '#'
        elif seats[nr][nc] == 'L':
            return 'L'
        nr += 1
        nc -= 1
    return '.'

def five_or_more_occupied(seats, row, col):
    count = 0
    res = check_up(seats, row, col)
    if res == '#':
        count += 1

    res = check_down(seats, row, col)
    if res == '#':
        count += 1
    
    res = check_left(seats, row, col)
    if res == '#':
        count += 1
    
    res = check_right(seats, row, col)
    if res == '#':
        count += 1
    
    res = check_up_left(seats, row, col)
    if res == '#':
        count += 1
    
    res = check_up_right(seats, row, col)
    if res == '#':
        count += 1
    
    res = check_bottom_left(seats, row, col)
    if res == '#':
        count += 1
    
    res = check_bottom_right(seats, row, col)
    if res == '#':
        count += 1

    return count >= 5

if __name__ == '__main__':
    main()
