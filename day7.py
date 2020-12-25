import re

def main():
    f = open('day7.txt', 'r')

    dic = {}

    for line in f:
        line = line.strip()
        
        bag_info = re.split('\\d', line)
        counts  = re.split('\\D+', line)

        counts = [x for x in counts if len(x.strip()) > 0]

        key = bag_info[0].strip()
        key = key.split()
        key = ' '.join([key[0], key[1]])

        dic[key] = []

        for i in range(1, len(bag_info)):
            val = bag_info[i].split()
            val = ' '.join([val[0], val[1]])

            dic[key].append(counts[i-1])
            dic[key].append(val)
    
    
    res = compute(dic, 'shiny gold')
    print(res)


def compute(dic, key):
    if len(dic[key]) == 0:
        print(key, 0)
        return 0

    index = 0
    config = dic[key]
    sm  = 0

    while index < len(config):
        count = int(config[index])
        index += 1
        n_key = config[index]

        sm += count + count * compute(dic, n_key)
        index += 1
    
    print(key, sm)
    return sm

if __name__ == '__main__':
    main()