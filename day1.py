items = []

def main():
    f = open("input1.txt", "r")

    for n in f:
        items.append(int(n.strip()))
    
    for n in items:
        res = doDoubleSum(2020-n)
        if len(res) == 2:
            print(n, res[0], res[1])
            break
    print('done')

def doDoubleSum(sm):
    nums = []

    for i in items:
        if i in nums:
            return [i, sm-i]
        else:
            nums.append(sm-i)
    return []


if __name__ == '__main__':
    main()