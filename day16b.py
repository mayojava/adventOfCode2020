import functools

def main():
    f = open('day16.txt', 'r')

    ranges = []
    range_map = {}
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
            range_map[line[0]] = line[1].strip()
            line = line[1].strip()
            line = line.split('or')
            line = [l.strip() for l in line]
            ranges += line
        elif current_read == 2:
            your_ticket = line
        else:
            nearby_tickets.append(line.strip())

    
    ranges = sorted(ranges, key=functools.cmp_to_key(compare))
    valid_nearby_tickets = []
    
    for nb in nearby_tickets:
        nbs = nb.split(',')
        nbs = [int(n) for n in nbs]
        valid = True

        for val in nbs:
            if not in_range(ranges, val):
                valid = False
                break
        
        if valid:
            valid_nearby_tickets.append(nbs)

    
    groups = []
    for valid_ticket in valid_nearby_tickets:
        if len(groups) == 0:
            for val in valid_ticket:
                groups.append([val])
        else:
            for idx, val in enumerate(valid_ticket):
                groups[idx].append(val)

    tickets = {}
    already_category = []
    not_assigned_groups = []

    for idx, group in enumerate(groups):
        categories = {}
        g_key = ''

        for value in group:
            g_key += str(value) + ' '
            possible_categories = get_possible_categories(value, range_map)

            for poss in possible_categories:
                if poss in categories:
                    categories[poss] += 1
                else:
                    categories[poss] = 1
        
        agreed_to_be_in_category = []
        
        for cat in categories:
            if categories[cat] == len(group):
                agreed_to_be_in_category.append(cat)
    
        g_key = g_key.strip()
        tickets[idx] = agreed_to_be_in_category
        if len(agreed_to_be_in_category) == 1:
            already_category.append(agreed_to_be_in_category[0])
        else:
            not_assigned_groups.append(agreed_to_be_in_category)
        
    ct = 0
    
    while True:
        current_key = already_category[-1]
        items_to_remove = []
        if ct == 20: break
        print(current_key)
        
        dict_keys = list(tickets.keys())
        dict_values = list(tickets.values())

        for idx, una in enumerate(not_assigned_groups):
            group_index = dict_keys[dict_values.index(una)]

            if current_key in una:
                una.remove(current_key)

            if len(una) == 1:
                items_to_remove.append(idx)
                already_category.append(una[0])
                tickets[group_index] = una
        
        for it in items_to_remove:
            not_assigned_groups.pop(it)
        
        ct+= 1

    your_ticket = [int(x) for x in your_ticket.split(',')]
    res = 1
    for key, value in tickets.items():
        if value[0].startswith('departure'):
            print(value, your_ticket[key])
            res *= your_ticket[key]
    print(res)

def get_possible_categories(val, ranges):
    res = []
    for key in ranges:
        values = ranges[key]
        values = values.split('or')

        for item in values:
            item = item.strip().split('-')
            begin = int(item[0])
            end = int(item[1])

            if val >= begin and val <= end:
                res.append(key)
                break
    return res


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
