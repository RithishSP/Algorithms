from time import time

# Solving using Kosaraju's SCC algorithm
# Function to load graph
def LoadGraph(filename):
    graph = {}
    with open (filename) as file:
        n = int(file.readline())  # Number of variables and clauses
        for line in file:
            a, b = map(int, line.strip().split())
            # Add the 2 cases to the graph
            graph.setdefault(-a, []).append(b)
            graph.setdefault(-b, []).append(a)
            # Make sure a and b are also in graph
            graph.setdefault(a , [])
            graph.setdefault(b , [])
    return graph

# Reverse of the Original Graph
def ReverseGraph(graph):
    revgraph = {}
    for node in graph:
        revgraph.setdefault(node, [])
        for neighbour in graph[node]:
            revgraph.setdefault(neighbour, []).append(node)
    return revgraph

# One DFS function for both runs
def DepthFirstSearch(node, graph, order, visited , mode): 
    complete = set()
    stack = [node] # Initialises start of DFS
    component = []  
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
    visited = set()  # Re-initialising visited to clean last DFS
    while order:
        node = order.pop()
        if node not in visited:
            component = DepthFirstSearch(node, graph, [], visited , False)  
            components.append(component)
    # Returning components
    return components

# Function to return 1 or 0 if its satisfiable or not
def TwoSAT(filename):
    graph = LoadGraph(filename)
    sccs = Kosaraju(graph)

    for component in sccs:
        componentSet = set(component)
        for variable in component:
            if -variable in componentSet:
                return 0
    return 1

# Initialising
startTime = time()
output = []
inputs = ['2SATDataSet1.txt',
          '2SATDataSet2.txt',
          '2SATDataSet3.txt',
          '2SATDataSet4.txt',
          '2SATDataSet5.txt',
          '2SATDataSet6.txt']
# Computing answers
for input in inputs:
    output.append(TwoSAT(input))
print(''.join(map(str,output)))
# Compute and display running time
totalTime = time() - startTime
minutes = int(totalTime // 60)
seconds = totalTime % 60
print(f"Execution time: {minutes} mins and {seconds:.2f} secs")

# Ans = 101100
# Execution time is around 1 minute