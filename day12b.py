def main():
    f = open('day12.txt', 'r')

    ship = {}
    waypoint = {'e':10, 'n':1}

    curr_n_s = 'n'
    curr_e_w = 'e'

    ship_n_s = ''
    ship_e_w = ''

    for line in f:
        line = line.strip()

        d = line[0]
        val = int(line[1:])

        if d == 'F':
            mv_n_s = abs(waypoint[curr_n_s] * val)
            mv_e_w = abs(waypoint[curr_e_w] * val)

            if len(ship) == 0:
                ship[curr_n_s] = mv_n_s
                ship[curr_e_w] = mv_e_w
                
                ship_n_s = curr_n_s
                ship_e_w = curr_e_w
            else: 

                n_ship_pos = {}
                np1 = 0
                np2 = 0

                if curr_n_s == 'n':
                    np1 = ship[ship_n_s] + mv_n_s
                elif curr_n_s == 's':
                    np1 = ship[ship_n_s] - mv_n_s

                if curr_e_w == 'e':
                    np2 = ship[ship_e_w] + mv_e_w
                else:
                    np2 = ship[ship_e_w] - mv_e_w

                if np2 > 0:
                    n_ship_pos['e'] = np2
                    ship_e_w = 'e'
                elif np2 < 0:
                    n_ship_pos['w'] = np2
                    ship_e_w = 'w'
                else:
                    n_ship_pos[curr_e_w] = np2
                    ship_e_w = curr_e_w

                if np1 > 0:
                    n_ship_pos['n'] = np1
                    ship_n_s = 'n'
                elif np1 < 0:
                    n_ship_pos['s'] = np1
                    ship_n_s = 's'
                else:
                    n_ship_pos[curr_n_s] = np1
                    ship_n_s = curr_n_s

                ship = n_ship_pos
        
        elif d == 'L' or d == 'R':
            keys = waypoint.keys()
            new_way_point = {}

            for k in keys:
                nf = new_facing(k, d, val)
                unit = waypoint[k]
                
                if nf == 'n' or nf == 's':
                    curr_n_s = nf
                    if curr_n_s == 'n':
                        new_way_point[curr_n_s] = abs(unit)
                    else:
                        new_way_point[curr_n_s] = -1*abs(unit)
                else:
                    curr_e_w = nf
                    if curr_e_w == 'e':
                        new_way_point[curr_e_w] = abs(unit)
                    else:
                        new_way_point[curr_e_w] = -1*abs(unit)
            
            waypoint = new_way_point
        
        elif d == 'S':
            dist = waypoint[curr_n_s] - val
            if dist <= 0:
                curr_n_s = 's'
                waypoint[curr_n_s] = dist
                waypoint.pop('n', None)
            else:
                curr_n_s = 'n'
                waypoint[curr_n_s] = dist
                waypoint.pop('s', None)

        elif d == 'N':
            dist = waypoint[curr_n_s] + val
            if dist >= 0:
                curr_n_s = 'n'
                waypoint[curr_n_s] = dist
                waypoint.pop('s', None)
            else:
                curr_n_s = 's'
                waypoint[curr_n_s] = dist
                waypoint.pop('n', None)

        elif d == 'E':
            dist = waypoint[curr_e_w] + val
            if dist >= 0:
                curr_e_w = 'e'
                waypoint[curr_e_w] = dist
                waypoint.pop('w', None)
            else:
                curr_e_w = 'w'
                waypoint[curr_e_w] = dist
                waypoint.pop('e', None)

        else:
            dist = waypoint[curr_e_w] - val
            if dist <= 0:
                curr_e_w = 'w'
                waypoint[curr_e_w] = dist
                waypoint.pop('e', None)
            else:
                curr_e_w = 'e'
                waypoint[curr_e_w] = dist
                waypoint.pop('w', None)

    r1 = ship[ship_n_s]
    r2 = ship[ship_e_w]

    print(abs(r1) + abs(r2))

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