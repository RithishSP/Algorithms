from heapq import heappush,heapify,heappop

# NOTE : I have deleted the first line in the dataset as it was unnecessary
# Function to Load Graph
def LoadGraph():
    with open("PrimMSTDataSet.txt") as file:
        graph = {}
        for line in file:
            v1 , v2 , weight = map(int, line.strip().split())
            # Building graph
            graph.setdefault(v1, []).append((v2 , weight))
            graph.setdefault(v2 , []).append((v1 , weight))
    return graph 

# Prim's MST algorithm
def PrimMST (graph):
    # Initialising
    source = list(graph.keys())[0]
    visitedNodes , totalCost = {source} , 0
    # Making heap of unvisited edges with neighbours of the source
    unvisitedEdges = [(weight,neighbour) for neighbour , weight in graph[source]]
    heapify(unvisitedEdges)
    # Main while loop
    while visitedNodes != set(graph.keys()): 
        # Getting minimum weight edge
        weight , newNode = heappop(unvisitedEdges)
        # Adding new node if its not in visited nodes
        if newNode not in visitedNodes:
            visitedNodes.add(newNode)
            totalCost+= weight # Updating total cost with the weight of edge added
            for neighbour, cost in graph[newNode]: # Updating neighbours and adding it to heap 
                if neighbour not in visitedNodes:
                    heappush(unvisitedEdges, (cost,neighbour))
        # Contine if new node is already in visited
        else:
            continue
    # Returning total cost of MST
    return totalCost

# Computing answer     
graph = LoadGraph()
print(PrimMST(graph))

# Ans = -3612829