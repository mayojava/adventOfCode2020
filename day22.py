def main():
    f = open('day22.txt', 'r')

    player_1 = []
    player_2 = []

    read = 1
    for line in f:
        if line.strip().startswith('Player 2'):
            read = 2
            continue
        elif line.strip().startswith('Player 1') or len(line.strip()) == 0: continue

        line = int(line.strip())
        if read == 1:
            player_1.append(line)
        else:
            player_2.append(line)

    while len(player_1) > 0 and len(player_2) > 0:
        if player_1[0] > player_2[0]:
            do_winner(player_1, player_2)
        else:
            do_winner(player_2, player_1)
    
    
    if len(player_1) > 0:
        print(get_res(player_1))
    else:
        print(get_res(player_2))

def do_winner(a, b):
    loser_card = b.pop(0)
    winner_card = a.pop(0)

    a.append(winner_card)
    a.append(loser_card)

def get_res(player):
    print(player)
    sm = 0
    mult = len(player)

    for i in player:
        sm += mult * i
        mult -= 1
    
    return sm
if __name__ == "__main__":
    main()