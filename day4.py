validEcls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def main():
    f = open('day4.txt', 'r')
    
    count = 0
    validcats = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    catForPassPort = []

    for line in f:
        if len(line.strip()) != 0:
            row = line.strip().split()

            for cats in row:
                cat = cats.split(':')[0]

                if cat == 'cid':
                    continue
                else:
                    if cat in validcats and cat not in catForPassPort and validate(cats):
                        catForPassPort.append(cat)
        else:
            if len(catForPassPort) == 7:
                count+=1
            catForPassPort.clear()
    
    
    if len(catForPassPort) == 7:
        count+=1
    
    print(count)

def validate(cat):
    csplit = cat.split(":")
    catname = csplit[0].strip()
    val = csplit[1].strip()

    if catname == 'byr':
        val = int(val)
        if val >= 1920 and val <= 2002:
            return True
        return False
    elif catname == 'iyr':
        val = int(val)
        if val >= 2010 and val <= 2020:
            return True
        return False
    elif catname == 'eyr':
        val = int(val)
        if val >= 2020 and val <= 2030:
            return True
        return False
    elif catname == 'hgt':
        if 'in' in val:
            acval = int(val.split('in')[0])
            if acval >= 59 and acval <= 76:
                return True
            return False
        elif 'cm' in val:
            acval = int(val.split('cm')[0])
            if acval >= 150 and acval <= 193:
                return True
            return False
        return False
    elif catname == 'hcl':
        if validHcl(val):
            return True
        return False
    elif catname == 'ecl':
        return val in validEcls
    elif catname == 'pid':
        return len(val) == 9
    
    return False


def validHcl(hcl):
    valchars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

    if len(hcl) != 7:
        return False
    if hcl[0] != '#':
        return False

    for ind in range(1,len(hcl)):
        if hcl[ind] not in valchars:
            return False
    return True

if __name__ == '__main__':
    main()