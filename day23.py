def main():
    cups = '952316487'
    cups = list(cups)
    cups = [int(x) for x in cups]

    sorted_version = cups.copy()
    sorted_version = sorted(sorted_version)

    current = 0
    for i in range(0, 100):
        print('cups', cups)
        cup = cups[current]
        removed = []
        to_rem = current+1

        for j in range(0, 3):
            if to_rem >= len(cups):
                to_rem = 0
            removed.append(cups[to_rem])
            to_rem += 1
        print('pick up', removed)

        for item in removed:
            cups.remove(item)
        #print('after', cups)

        destination = cup-1
        if destination < sorted_version[0]:
            destination = sorted_version[-1]

        while destination in removed:
            destination -= 1
            if destination < sorted_version[0]:
                destination = sorted_version[-1]
        

        index_of_destination = cups.index(destination)
        print('destination', destination, 'index', index_of_destination)
        
        index_of_destination += 1
        for item in removed:
            cups.insert(index_of_destination, item)
            index_of_destination += 1
        
        while cups.index(cup) != current:
            rem = cups.pop(0)
            cups.append(rem)
        
        print()
        current += 1

        if current >= len(cups): current = 0
    
    print(cups)

    index_of_one = cups.index(1)
    start = index_of_one + 1

    string = ''
    while cups[start] != 1:
        string += str(cups[start])
        start += 1

        if start >= len(cups): start = 0
    
    print(string)



if __name__ == "__main__":
    main()