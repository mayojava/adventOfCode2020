def main():
    f = open("day2.txt", "r")
    count = 0

    for line in f:
        if isValid(line.strip()):
            #print(line)
            count+=1

    print(count)

def isValid(line):
    split = line.split(":")
    password = split[1].strip()
    rule = split[0].split()

    char = rule[1].strip()
    minmax = rule[0].split("-")

    min = int(minmax[0]) - 1
    max = int(minmax[1]) - 1

    inFIndex = password[min] == char
    inSIndex = password[max] == char

    #print(min, max, inFIndex, inSIndex, password[min], password[max])

    if inFIndex and inSIndex:
        return False
    elif inFIndex == False and inSIndex == False:
        return False
    return True

if __name__ == '__main__':
    main()
