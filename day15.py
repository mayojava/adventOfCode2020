def main():
    f = open('day15.txt', 'r')

    for line in f:
        line = line.strip()
        line = line.split(',')
        line = [int(x) for x in line]

        mem = {}
        index = 1
        total = 30000000
        last_spoken = -1

        for i in range(0, len(line)):
            last_spoken = line[i]

            if last_spoken in mem:
                mem[last_spoken].append(index)
                if len(mem[last_spoken]) > 2:
                    mem[last_spoken].pop(0)
            else:
                mem[last_spoken] = [index]
            
            index += 1
            total -= 1
        

        while total != 0:
            print(index)
            if len(mem[last_spoken]) == 1:
                last_spoken = 0
            else:
                last_spoken = mem[last_spoken][-1] - mem[last_spoken][-2]

            if last_spoken not in mem:
                mem[last_spoken] = [index]
            else:
                mem[last_spoken].append(index)
                if len(mem[last_spoken]) > 2:
                    mem[last_spoken].pop(0)
            
            index += 1
            total -= 1
        
        print(last_spoken)
        #print(mem)
        break





if __name__ == '__main__':
    main()