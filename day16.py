import functools

def main():
    f = open('day16.txt', 'r')

    ranges = []
    your_ticket = ''
    nearby_tickets = []

    current_read = 1

    for line in f:
        line = line.strip()

        if len(line) == 0:
            continue
        
        if line.startswith('your ticket'):
            current_read = 2
            continue
        elif line.startswith('nearby tickets'):
            current_read = 3
            continue
        
        if current_read == 1:
            line = line.split(':')
            line = line[1].strip()
            line = line.split('or')
            line = [l.strip() for l in line]
            ranges += line
        elif current_read == 2:
            your_ticket = line
        else:
            nearby_tickets.append(line.strip())

    
    
    ranges = sorted(ranges, key=functools.cmp_to_key(compare))
    
    sm = 0
    for nb in nearby_tickets:
        nbs = nb.split(',')
        nbs = [int(n) for n in nbs]

        for val in nbs:
            if not in_range(ranges, val):
                sm += val

    
    print(sm)
    #print(ranges)
    #print(your_ticket)
    #print(nearby_tickets)

def in_range(ranges, v):
    res = False

    for r in ranges:
        r = r.split('-')
        begin = int(r[0])
        end = int(r[1])

        if v > end:
            continue
        else:
            begin_after_start = begin > v
            if begin_after_start:
                res = False
                break
            else:
                res = True
                break
    return res

def compare(item1, item2):
    begin1 = int(item1.split('-')[0])
    begin2 = int(item2.split('-')[0])

    if begin1 < begin2: return -1
    if begin1 > begin2: return 1
    return 0

if __name__ == '__main__':
    main()
