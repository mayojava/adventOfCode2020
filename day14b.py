import re
import itertools

def main():
    f = open('day14.txt', 'r')

    mask = ''
    mems = {}
    sm = 0

    for line in f:
        line = line.strip()

        if line.startswith('mask'):
            line = line.split('=')
            mask = line[1].strip()
        else:
            line = line.split('=')
            num = int(line[1].strip())
            address = line[0].strip()
            
            address = re.search('[0-9]+', address)
            address = address.group()

            mask_list = list(mask)
            address_list = list(dec_bin(int(address)))
            floating_indexes = []

            for index in range(0, 36):
                if mask_list[index] == '1':
                    address_list[index] = '1'
                elif mask_list[index] == 'X':
                    floating_indexes.append(index)
                    address_list[index] = 'X'
            
            bits = list(map(list, itertools.product([0,1], repeat=len(floating_indexes))))

            for bit in bits:
                for idx in range(0,len(bit)):
                    address_list[floating_indexes[idx]] = str(bit[idx])
                
                address_string = ''.join(address_list)
                address_location = bin_dec(address_string)

                if address_location in mems:
                    sm -= mems[address_location]
                    mems[address_location] = num
                    sm += mems[address_location]
                else:
                    mems[address_location] = num
                    sm += mems[address_location]
    
    print(mems)
    print('sum', sm)



def bin_dec(bin):
    return int(bin, 2)

def dec_bin(dec):
    return format(dec, '036b')


if __name__ == '__main__':
    main()