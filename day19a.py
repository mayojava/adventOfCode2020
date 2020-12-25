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
    
    cache = {}
    rule_zero = decipher('0', rule_map, cache)

    count = 0
    for msg in messages:
        if msg.strip() in rule_zero:
            count+=1
    
    print(count)

def decipher(rule, map, cache = {}):
    if rule in cache:
        return cache[rule]

    if len(map[rule]) == 1: #base case is number with one rule
        cache[rule] = [map[rule]]
        return [map[rule]]
    
    rules = map[rule]
    rules = rules.split("|")
    
    res = []

    for r in rules:
        r = r.strip().split()
        splitted = [x.strip() for x in r if len(x.strip()) > 0]
        
        concat_res = decipher(splitted[0], map, cache)
        for rem in range(1, len(splitted)):
            result = decipher(splitted[rem], map, cache)
            concat_res = cross(concat_res, result)
        
        for item in concat_res:
            res.append(item)
    
    cache[rule] = res
    return res

def cross(a, b):
    res = []
    for i in a:
        for j in b:
            res.append(i+j)
    return res

if __name__ == "__main__":
    main()