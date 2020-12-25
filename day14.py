import re

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

            if mask == '':
                if address in mems:
                    sm -= mems[address]
                    sm += num
                    mems[address] = num
                else:
                    mems[address] = num
                    sm += num
            else:
                mask_list = list(mask)
                num_list = list(dec_bin(num))

                for index in range(0, 36):
                    if mask_list[index] != 'X' and mask_list[index] != num_list[index]:
                        num_list[index] = mask_list[index]
                
                bin_string = ''.join(num_list)
                updated_number = bin_dec(bin_string)

                print('writing', updated_number)

                if address in mems:
                    sm -= mems[address]
                    sm += updated_number
                    mems[address] = updated_number
                else:
                    mems[address] = updated_number
                    sm += updated_number

    print('sum', sm)



def bin_dec(bin):
    return int(bin, 2)

def dec_bin(dec):
    return format(dec, '036b')


if __name__ == '__main__':
    main()