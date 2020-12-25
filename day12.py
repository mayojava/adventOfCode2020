def main():
    f = open('day12.txt', 'r')

    current = {'e/w': 'e', 'n/s': 'n'}
    dic = {'e':0, 'w':0, 's':0, 'n':0}

    facing = 'e'

    for line in f:
        line = line.strip()

        d = line[0]
        val = int(line[1:])

        if d == 'F':
            if facing == 'n' or facing == 's': 
                dist = dic[current['n/s']]
                if facing == 'n':
                    dist += val
                else:
                    dist -= val

                if dist < 0:
                    dic['n'] = 0
                    dic['s'] = dist
                    current['n/s'] = 's'
                else:
                    dic['s'] = 0
                    dic['n'] = dist
                    current['n/s'] = 'n'
            else:
                dist = dic[current['e/w']]
                if facing == 'e':
                    dist += val
                else:
                    dist -= val

                if dist < 0:
                    dic['e'] = 0
                    dic['w'] = dist
                    current['e/w'] = 'w'
                else:
                    dic['w'] = 0
                    dic['e'] = dist
                    current['e/w'] = 'e'

            #print(current)
            #print(dic)
        
        elif d == 'L' or d == 'R':
            nf = new_facing(facing, d, val)
            facing = nf
        
        elif d == 'S':
            dist = dic[current['n/s']]
            dist -= val

            if dist < 0:
                current['n/s'] = 's'
                dic['n'] = 0
                dic['s'] = dist
            else:
                dic['n'] = dist
                dic['s'] = 0
                current['n/s'] = 'n'

        elif d == 'N':
            dist = dic[current['n/s']]
            dist += val

            if dist >= 0:
                current['n/s'] = 'n'
                dic['s'] = 0
                dic['n'] = dist
            else:
                dic['s'] = dist
                dic['n'] = 0
                current['n/s'] = 's'

        elif d == 'E':
            dist = dic[current['e/w']]
            dist += val

            if dist >= 0:
                current['e/w'] = 'e'
                dic['w'] = 0
                dic['e'] = dist
            else:
                current['e/w'] = 'w'
                dic['w'] = dist
                dic['e'] = 0

        else:
            dist = dic[current['e/w']]
            dist -= val

            if dist < 0:
                current['e/w'] = 'w'
                dic['w'] = dist
                dic['e'] = 0
            else:
                current['e/w'] = 'e'
                dic['w'] = 0
                dic['e'] = dist
    
    #print(current)
    print(abs(dic[current['e/w']]), abs(dic[current['n/s']]))
    print(abs(dic[current['e/w']]) + abs(dic[current['n/s']]))

def new_facing(facing, d, val):
    if facing == 'e':
        if d == 'L':
            if val == 90:
                return 'n'
            if val == 180:
                return 'w'
            if val == 270:
                return 's'
        else:
            if val == 90:
                return 's'
            if val == 180:
                return 'w'
            if val == 270:
                return 'n'
        return 'e'
    elif facing == 'w':
        if d == 'L':
            if val == 90:
                return 's'
            if val == 180:
                return 'e'
            if val == 270:
                return 'n'
        else:
            if val == 90:
                return 'n'
            if val == 180:
                return 'e'
            if val == 270:
                return 's'
        return 'w'
    elif facing == 'n':
        if d == 'L':
            if val == 90:
                return 'w'
            if val == 180:
                return 's'
            if val == 270:
                return 'e'
        else:
            if val == 90:
                return 'e'
            if val == 180:
                return 's'
            if val == 270:
                return 'w'
        return 'n'
    else:
        if d == 'L':
            if val == 90:
                return 'e'
            if val == 180:
                return 'n'
            if val == 270:
                return 'w'
        else:
            if val == 90:
                return 'w'
            if val == 180:
                return 'n'
            if val == 270:
                return 'e'
        return 's'

        


if __name__ == '__main__':
    main()