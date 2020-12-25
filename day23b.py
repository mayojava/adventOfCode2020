def main():
    cups = '952316487'
    cups = list(cups)
    cups = [int(x) for x in cups]

    for cup in range(10, 1000000+1):
        cups.append(cup)

    circ = CircularList()

    for x in cups:
        circ.addNode(x)
    
    map = {}
    current = circ.firstCup
    map[current.value] = current

    iter(current)

    for i in range(1, len(cups)):
        current = current.next
        map[current.value] = current

    removed = []

    for i in range(0, 10000000):
        current_value = circ.currentCup.value
        #write_cup = circ.firstCup

        for j in range(0, 3):
            removed.append(circ.currentCup.next)
            circ.currentCup.next = circ.currentCup.next.next
        
        remm = ''
        for ff in removed:
            remm += str(ff.value) + " "
        print('removing', remm)

        destination = current_value
        while True:
            destination -= 1
            if destination == 0:
                destination = 1000000
                #destination = 9
                
            in_removed = False
            for x in removed:
                if x.value == destination:
                    in_removed = True
                    break
                
            if not in_removed: break

        destination_node = map[destination]
        for i in range(0,3):
            removed[i].next = destination_node.next
            destination_node.next = removed[i]
            destination_node = removed[i]
        
        removed = []
        circ.currentCup = circ.currentCup.next

    one_node = map[1]
    print('first next of 1', one_node.next.value)
    print('second next of 1', one_node.next.next.value)
    print('mult', one_node.next.value * one_node.next.next.value)

    #string = ''
    #for i in range(0, 8):
      #  one_node = one_node.next
     #   string += str(one_node.value)
    #print(string)

def iter(root):
    copy = root
    string = ''
    for i in range(0, 10):
        string += str(copy.value)
        copy = copy.next
    print('------ list -----', string)


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.previous = None

class CircularList:
    def __init__(self):
        self.currentCup = None
        self.firstCup = None
        self.lastCup = None

    def addNode(self, val):
        if self.currentCup is None:
            self.currentCup = Node(val)
            self.firstCup = self.currentCup
            self.lastCup = self.currentCup
        else:
            self.lastCup.next = Node(val)
            self.lastCup = self.lastCup.next
            self.lastCup.next = self.firstCup

if __name__ == "__main__":
    main()
