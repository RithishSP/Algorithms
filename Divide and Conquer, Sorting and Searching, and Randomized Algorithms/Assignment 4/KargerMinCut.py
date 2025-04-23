import random 

def LoadGraph():
    graph = {}
    with open('kargerMinCutDataSet.txt') as file:
        for i in file:
            line = i.split()
            if line:
                vertices = [int(x) for x in line[1:]]
                graph[int(line[0])] = vertices
    return graph

def RandomVertices (graph):
    v1 = list(graph.keys())[random.randint(0,len(graph)-1)] # Any random vertext of the graph
    v2 = list(graph[v1])[random.randint(0,len(graph[v1])-1)] # Random vertex which has an edge with the first vertex
    return v1 , v2

def Merge (graph , v):

    v1 = graph[v[0]]  
    v1.extend(graph[v[1]])  # Merging
    del graph[v[1]] # Deletion of the merged vertex

    for i in graph.keys():
        graph[i] = [v[0] if x == v[1] else x for x in graph[i]] # Merging all edges of v2 to v1
    
    graph[v[0]] = [j for j in graph[v[0]] if j!=v[0]] # Deleting self loops

graph = LoadGraph()
n = len(graph)
cut = len(graph[list(graph.keys())[0]])  # Declaring mincut

for i in range (0,2*n+1):
    graph = LoadGraph()
    while len(graph) > 2:
        Merge(graph , RandomVertices(graph))
    if cut > len(graph[list(graph.keys())[0]]):
        cut = len(graph[list(graph.keys())[0]])
    if i%50 == 0 and i != 0: # Printing every 50 mincuts computed to see if minimum remains same or reduces
        print(cut)

#Ans = 17

'''
    I used a big enough number of iterations for the answer in this case, but generally n*n*log(n)
can be used to get a good approximation of the answer.
https://www.cs.princeton.edu/courses/archive/fall13/cos521/lecnotes/lec2final.pdf
    There are other improvements such as the Karger-Stein improvement or assigning each
edge a random weight and using Kruskal's MST algorithm to break the largest edge to get the largest
clusters which I have not implemented here. 

'''
