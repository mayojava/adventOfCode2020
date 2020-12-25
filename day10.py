def main():
    f = open('day10.txt', 'r')

    nums = [0]

    for line in f:
        line = int(line.strip())
        nums.append(line)
    nums = sorted(nums)
    print(nums)

    graph = {}
    for i in nums:
        if i not in graph:
            graph[i] = []

        if i+1 in nums:
            if i+1 not in graph:
                graph[i+1] = []
            graph[i+1].append(i)


        if i+2 in nums:
            if i+2 not in graph:
                graph[i+2] = []
            graph[i+2].append(i)

        if i+3 in nums:
            if i+3 not in graph:
                graph[i+3] = []
            graph[i+3].append(i)
    
    print(doWay(graph, nums[-1], {}))

def doWay(graph, item, done):
    sm = 0

    conn = graph[item]
    if len(conn) == 0:
        return 1

    if item in done:
        return done[item]
    
    for val in conn:
        sm += doWay(graph, val, done)
    
    done[item] = sm
    print(done)
    return sm
        

    
    #g = Graph()
    #for n in nums:
     #   g.add(n)
    
    #vis = {}
    #for node in g.nodes:
     #   vis[node] = []

      #  if  node+1 in g.nodes:
       #     g.addNode(node, node+1)
        #if node+2 in g.nodes:
         #   g.addNode(node, node+2)
       # if node+3 in g.nodes:
        #    g.addNode(node, node+3)

   # ways = {}
   # ways[nums[0]] = 1
    #ways[nums[-1]] = 1

        
    
    #ls = []
    #memo = {}
    #dfs([nums[0]], vis, g, nums[-1], ls, memo)
    #print(len(ls))

def dfs(stack, vis, g, max, ls):
    while len(stack) > 0:
        #print(stack)
        top = stack[-1]
        if top == max:
            print(1)
            #ls.append(1)
            stack.pop()
            return 

        res = unvisited(top, vis, g.nodes[top])
        if res != -1:
            vis[top].append(res)
            stack.append(res)
            dfs(stack, vis, g, max, ls)
        else:
            vis[top] = []
            stack.pop()

def unvisited(start, vis, conns):
    for con in conns:
        if con not in vis[start]:
            return con
    return -1




class Graph:
    nodes = {}
    
    def add(self, val):
        self.nodes[val] = []

    def addNode(self, key, val):
        self.nodes[key].append(val)

if __name__ == '__main__':
    main()