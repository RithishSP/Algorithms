# Inputting graph
def LoadGraph():
    graph = {}
    for node in range(875714):
        graph[node+1] = []
    with open('KosarajuSCCDataSet.txt') as file:
        for line in file:
            node, neighbour = line.split()
            graph[int(node)].append(int(neighbour))  
    return graph

# Reverse of the Original Graph
def ReverseGraph(graph):
    revgraph = {}
    for node in graph:
        revgraph[node] = []  # Mapping nodes of graph to revgraph
    for node in graph:
        for neighbour in graph[node]:  
            revgraph[neighbour].append(node)  
    return revgraph

# One DFS function for both runs decided by mode
def DepthFirstSearch(node, graph, order, visited , mode):  
    stack = [node] # Initialises start of DFS
    component = []  
    complete = set()
    while stack:
        node = stack[-1] # Last added node
        if node not in visited: 
            visited.add(node) 
            for neighbour in graph[node]:
                if neighbour not in visited: # Add unvisited neighbour to stack
                    stack.append(neighbour)
        else:
            stack.pop()
            if node not in complete:
                complete.add(node) 
                if mode:
                    order.append(node) # For reverse DFS
                else:
                    component.append(node) # For original DFS
    if not mode:
        return component  

def Kosaraju(graph):
    visited = set()
    components = []
    order = [] 
    # Making revgraph 
    revgraph = ReverseGraph(graph)
    # DFS on Reverse Graph
    for node in graph:
        if node not in visited:
            DepthFirstSearch(node, revgraph, order, visited , True)  
    # DFS on Original Graph
    visited = set()  # Re-initialising visited and complete to clean last DFS
    while order:
        node = order.pop()
        if node not in visited:
            component = DepthFirstSearch(node, graph, [], visited , False)  
            components.append(component)
    # Returning components
    return components

# Computing answer
graph = LoadGraph()
components = Kosaraju(graph)
# Printing the 5 largest sizes of components
print(sorted([len(c) for c in components], reverse = True)[:5])

# Ans = [434821, 968, 459, 313, 211]