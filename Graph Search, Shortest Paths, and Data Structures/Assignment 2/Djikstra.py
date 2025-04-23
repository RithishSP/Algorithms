from heapq import heappush , heappop

# Getting weighted graph
def LoadGraph():
    graph = {}
    with open('DjikstraDataSet.txt') as file:
        for line in file:
            parts = line.strip().split()
            node = int(parts[0])
            graph[node] = []
            for pair in parts[1:]:
                neighbour, weight = map(int, pair.split(','))
                graph[node].append((neighbour, weight))
    return graph
 
def Djikstra( graph, source , end ):
    # Initialising
    distances = {}
    distances[source] = 0 
    heap = [(0, source , ())]
    visited = set()

    while heap: # Main Djikstra Loop
        (cost , node , path) = heappop(heap)
        if node in visited: # Check if node is visited
            continue
        visited.add(node) # Else add node and update path
        path = path + (node,)
        if node == end: # Return cost and path if end has been reached
            return cost , path
        for neighbour, weight in graph.get(node, None): # Checking neighbours weights
            previousCost = distances.get(neighbour, None)
            updatedCost = cost + weight
            if previousCost is None or updatedCost < previousCost: # Updating costs
                distances[neighbour] = updatedCost
                heappush(heap, (updatedCost, neighbour, path))
    return 1000000 , None # If path never reaches end

# Computing
graph = LoadGraph()
ends = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
minCosts = [Djikstra(graph , 1 , end)[0] for end in ends]
print(minCosts)

# Ans = [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]