def main2(inst, state):
    accum = 0
    index = 0
    #print('trying', inst)
    #print(state)

    while True:
        if index >= len(inst):
            print('accum is: ', accum)
            return accum

        if state[index]:
            #print(accum)
            return -1

        current = inst[index].split()
        ins = current[0].strip()
        count = int(current[1])

        #print(ins, count)

        if ins == 'nop':
            state[index] = True
            index += 1
            continue

        if ins == 'acc':
            accum += count
            state[index] = True
            index += 1
            continue

        if ins == 'jmp':
            state[index] = True
            index += count

def main():
    f = open('day8.txt', 'r')
    inst = []
    state = []

    for line in f:
        line = line.strip()
        inst.append(line)
        state.append(False)

    for lev in range(0,2):
        copy = inst.copy()

        for inst_index in range(0, len(copy)):
            if copy[inst_index].startswith('nop') and lev == 0:
                copy[inst_index] = copy[inst_index].replace('nop', 'jmp', 1)
            elif copy[inst_index].startswith('jmp') and lev == 1:
                copy[inst_index] = copy[inst_index].replace('jmp', 'nop', 1)
            else:
                continue

            state_copy = state.copy()
            res = main2(copy, state_copy)

            if res == -1:
                if copy[inst_index].startswith('nop'):
                    copy[inst_index] = copy[inst_index].replace('nop', 'jmp', 1)
                else:
                    copy[inst_index] = copy[inst_index].replace('jmp', 'nop', 1)
            else:
                print('halted at: ', res)
                #print(copy)
                return


            


if __name__ == '__main__':
    main()