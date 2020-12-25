import sys

def main():
    f = open('day13.txt', 'r')
    
    earliest_time = int(f.readline().strip())
    buses = f.readline().strip().split(',')
    buses = [int(x) for x in buses if x != 'x']

    closest_departure = [earliest_time//bus * bus for bus in buses]
    
    index = -1
    wait = sys.maxsize

    for idx, val in enumerate(closest_departure):
        if val == 0:
            index = idx
            wait = val
        else:
            next_time = val + buses[idx]
            waait_time = next_time - earliest_time

            if waait_time < wait:
                index = idx
                wait = waait_time

    
    print(wait * buses[index])
    #print(buses)
    #print(closest_departure)


if __name__ == '__main__':
    main()