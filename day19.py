import re

def main():
    f = open('day19.txt', 'r')

    rules = []
    messages = []

    read_rules = True
    for line in f:
        line = line.strip()
        
        if len(line) == 0:
            read_rules = False
            continue

        if read_rules:
            rules.append(line)
        else:
            messages.append(line)
    

    rule_map = {}
    for rule in rules:
        rule = rule.split(":")
        pattern = re.compile('a|b')
        res = pattern.search(rule[1].strip())
        if res == None:
            rule_map[rule[0]] = rule[1].strip()
        else:
            rule_map[rule[0]] = res.group()
    
    rd = {}
    rule_zero = decipher('0', rule_map, rd)
    
    rule_eight = decipher('8', rule_map)
    rule_eleven = decipher('11', rule_map)
    rule_42 = decipher('42', rule_map)
    rule_31 = decipher('31', rule_map)
    
    count = 0

    to_rem = []
    for msg in messages:
        if msg.strip() in rule_zero:
            count+=1
            to_rem.append(msg.strip())
    
    print(count)
    
    for rm in to_rem:
        messages.remove(rm)
    
    for current in messages:
        if first_check({42:rule_42, 11:rule_eleven, 31:rule_31}, current):
            count += 1
        elif second_check({42:rule_42, 31:rule_31}, current):
            count += 1
        elif third_check({42:rule_42, 31: rule_31}, current):
            count += 1
    
    print(count)
    print('done')


def first_check(map, rem):
    start = [42,42,42]
    thirty_one = 2

    while True:
        copy = start
        current = rem
        
        for i in copy:
            res = remove(i, current, map[i])
            if len(res) == 0: return False
            if len(res) == len(current): return False
            current = res
        
        cnt = 0
        while len(current) > 0:
            if cnt == thirty_one: break
            res = remove(31, current, map[31])
            if len(res) == len(current): break
            cnt+=1
            current = res
        
        if len(current) == 0 and cnt == thirty_one: return True
        start.append(42)
        thirty_one += 1


def second_check(map, rem):
    start = [42,42,42]

    while True:
        copy = start
        current = rem

        for i in copy:
            res = remove(i, current, map[i])
            if len(res) == 0: return False
            if len(res) == len(current): return False
            current = res
        
        res = remove(31, current, map[31])
        if len(res) == 0: return True

        start.append(42)

def third_check(map, rem):
    start = [42,42,42,42]

    while True:
        copy = start
        current = rem

        for i in copy:
            res = remove(i, current, map[i])
            if len(res) == 0: return False
            if len(res) == len(current): return False
            current = res
        
        
        cnt = 0
        while len(current) > 0:
            res = remove(31, current, map[31])
            if len(res) == len(current): break
            current = res
            cnt += 1
        
        if len(current) == 0:
            if len(start) == 4 and cnt == 2:
                return True
            if len(start) > 4 and cnt >=2:
                return True

        start.append(42)


def remove(i, string, m):
    start = 0
    while True:
        if start > len(string): return string

        substring = string[0:start]
        if substring in m: 
            return string[start:]
        else: start += 1
    return string

def do_copy_2(start, rev=False):
    copy = []
    for x in start:
        if x == 8:
            copy.append(42)
            if rev:
                copy.append(8)
        else:
            copy.append(x)
    return copy

def do_copy(start, rev=False):
    copy = []
    for x in start:
        if x == 11:
            copy.append(42)
            if rev:
                copy.append(11)
            copy.append(31)
        else:
            copy.append(x)
    return copy

def decipher(rule, map, already_done = {}):
    if rule in already_done:
        
        return already_done[rule]

    if len(map[rule]) == 1:
        already_done[rule] = [map[rule]]
        return [map[rule]]
    
    rules = map[rule]
    rules = rules.split("|")
    
    res = []

    for r in rules:
        r = r.strip().split()
        splitted = [x.strip() for x in r if len(x.strip()) > 0]
        
        concat_res = decipher(splitted[0], map, already_done)
        for rem in range(1, len(splitted)):
            result = decipher(splitted[rem], map, already_done)
            concat_res = cross(concat_res, result)
        
        for item in concat_res:
            res.append(item)
    
    already_done[rule] = res
    return res


def cross(a, b):
    res = []
    for i in a:
        for j in b:
            res.append(i+j)
    return res   
    
if __name__ == "__main__":
    main()
