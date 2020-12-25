def main():
    card_pub_key = 18499292
    doors_pub_key = 8790390

    loop_size_card = transform(card_pub_key)
    loop_size_door = transform(doors_pub_key)

    print(transform_with_loop(card_pub_key, loop_size_door))
    print(transform_with_loop(doors_pub_key, loop_size_card))


def transform_with_loop(key, count):
    val = 1
    for i in range(0, count):
        val *= key
        val = val % 20201227
    
    return val


def transform(key):
    initial = 7
    val = 1

    index = 0
    while True:
        val *= initial
        val = val % 20201227

        index += 1

        if val == key: break
    

    return index



if __name__ == '__main__':
    main()