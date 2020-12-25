lines = []

def check(r, d):
    row = 0
    col = 0
    count = 0

    while row+1 < len(lines):
        col = col + r
        if col >= len(lines[0]):
            col = col % len(lines[0])
        row += d

        #print(row, col)

        if lines[row][col].strip() == '#':
            count += 1

    return count

def main():
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    f = open('day3.txt', 'r')
    res = 1

    for line in f:
        lines.append(line.strip())

    for slope in slopes:
        res *= check(slope[0], slope[1])
    
    print(res)

if __name__ == '__main__':
    main()