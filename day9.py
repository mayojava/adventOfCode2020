def main():
    f = open('day9.txt', 'r')

    nums = []
    for line in f:
        nums.append(int(line.strip()))
    
    left = 0
    right = 24

    while right+1 < len(nums):
        isValid = isDoubleSum(nums[left:right+1], nums[right+1])
        #print('valid', isValid)
        if not isValid:
            print('invalid', nums[right+1])
            rs = find(nums, nums[right+1])
            print(rs[0] + rs[-1])
            return 
        
        left += 1
        right += 1

def find(nums, val):
    cont = []
    sm = 0

    for i in nums:
        cont.append(i)
        sm += i

        while sm > val:
            pop = cont.pop(0)
            sm -= pop
        
        if sm == val:
            return sorted(cont)
    return []


def isDoubleSum(nums, val):
    seen = []

    for i in nums:
        if i in seen:
            return True
        seen.append(val - i)
    return False


if __name__ == '__main__':
    main()