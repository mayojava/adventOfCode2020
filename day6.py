def main():
    f = open('day6.txt', 'r')

    acm = 0
    count = 0
    dic = {}

    for line in f:
        line = line.strip()

        if len(line) == 0:
            acm += findCommom(dic, count)
            count = 0
            dic.clear()
            continue

        addCount(dic, line)
        count += 1
    
    acm += findCommom(dic, count)
    print(acm)

def findCommom(dic, count):
    sm = 0
    for c in dic:
        if dic[c] == count:
            sm += 1
    print(sm)
    return sm

def addCount(dic, line):
    for c in line:
        if c in dic:
            dic[c] = dic[c] + 1
        else:
            dic[c] = 1

def findUnique(answer):
    lin = []

    for c in answer:
        if c not in lin:
            lin.append(c)
    return len(lin)


if __name__ == '__main__':
    main()