import sys
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
    
    winner = simulate(player_1, player_2, [], [])
    print(get_res(winner))


def simulate(player1, player2, state1, state2):
    while len(player1) > 0 and len(player2) > 0:

        if player1 in state1 or player2 in state2: return player1
        state1.append(player1.copy())
        state2.append(player2.copy())

        print(player1)
        print(player2)
        print('')

        p1_draw = player1.pop(0)
        p2_draw = player2.pop(0)

        if len(player1) >= p1_draw and len(player2) >= p2_draw:
            result = subgame(player1[0:p1_draw], player2[0:p2_draw], {}, 2)

            if result == 1:
                player1.append(p1_draw)
                player1.append(p2_draw)
            else:
                player2.append(p2_draw)
                player2.append(p1_draw)
        else:
            if p1_draw > p2_draw:
                player1.append(p1_draw)
                player1.append(p2_draw)
            else:
                player2.append(p2_draw)
                player2.append(p1_draw)

    
    if len(player1) == 0: return player2
    if len(player2) == 0: return player1

def subgame(p1, p2, cache, index):
    print('Game', index)
    cache[index] = [[], []]

    while len(p1) > 0 and len(p2) > 0:
        if p1 in cache[index][0] or p2 in cache[index][1]: return 1

        cache[index][0].append(p1.copy())
        cache[index][1].append(p2.copy())

        print(p1)
        print(p2)

        p1_draw = p1.pop(0)
        p2_draw = p2.pop(0)
        
        print('p1 draw', p1_draw)
        print('p2 draw', p2_draw)
        print('')

        if len(p1) >= p1_draw and len(p2) >= p2_draw:
            win = subgame(p1[0:p1_draw], p2[0:p2_draw], cache, index+1)
            if win == 1:
                p1.append(p1_draw)
                p1.append(p2_draw)
            else:
                p2.append(p2_draw)
                p2.append(p1_draw)
        else:
            if p1_draw > p2_draw:
                p1.append(p1_draw)
                p1.append(p2_draw)
            else:
                p2.append(p2_draw)
                p2.append(p1_draw)
    
    if len(p1) > 0: return 1
    else: return 2

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