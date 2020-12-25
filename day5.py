def main():
    f = open('day5.txt', 'r')

    max = 0
    li = []

    for line in f:
        line = line.strip()
        res = get_seat(line)
        if res > max:
            max = res
        li.append(res)
        #print(res)
    #li = sorted(li)
    
    k = max
    while True:
        if k not in li:
            print("not in: ", k)
            break
        k -= 1

    print(max)

def get_seat(line):
    row = get_row(line[:7])
    col = get_col(line[7:])
    res = (row * 8) + col
    #print(row, col, res)
    return res

def get_row(line):
    left = 0
    right = 127

    for i in line:
        if i == 'F':
            right = (left + right) // 2
        else:
            left = ((left + right) // 2) + 1

    if line[-1] == 'F':
        return left
    return right

def get_col(line):
    left = 0
    right = 7

    for i in line:
        if i == 'R':
            left = ((left + right) //2 ) + 1
        else:
            right = (left + right) // 2
    
    if line[-1] == 'L':
        return left
    return right

if __name__ == '__main__':
    main()