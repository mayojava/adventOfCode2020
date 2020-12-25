import functools

def main():
    f = open('day21.txt', 'r')

    allergens = {}
    ingridients = []
    ing_lines = []

    for line in f:
        line = line.strip()
        line = line.split('(')
        
        ings = line[0].strip()
        allergs = get_allergens(line[1])
        ing_lines.append(ings.split())

        for i in ings.split():
            if i not in ingridients:
                ingridients.append(i)

        for a in allergs:
            if a in allergens:
                allergens[a] = allergens[a].intersection(set(ings.split()))
            else:
                allergens[a] = set(ings.split())
        
    
    #print(ingridients)

    infected = {}
    to_pop = []
    while True:
        if len(allergens) == 0:
            break

        for key in to_pop:
            allergens.pop(key)
        to_pop = []

        for key in allergens:
            if len(allergens[key]) == 1:
                val = allergens[key].pop()
                infected[val] = key

                print('removing', key)
                to_pop.append(key)

                for other_keys in allergens:
                    if val in allergens[other_keys]:
                        allergens[other_keys].remove(val)

    #count = 0
    #for li in ing_lines:
     #   for l in li:
      #      if l not in infected:
       #         count += 1
    
    print(infected)
    d = dict(sorted(infected.items(), key=lambda item: item[1]))
    
    print(','.join(list(d.keys())))


def get_allergens(string):
    string = string[0:-1]
    string = string.split(',')

    allergs = []
    for idx, val in enumerate(string):
        if idx == 0:
            val = val.split()[1]
            allergs.append(val)
        else:
            val = val.strip()
            allergs.append(val)
    
    return allergs

if __name__ == "__main__":
    main()