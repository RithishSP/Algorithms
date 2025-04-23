from UnionFind import UnionFind

# NOTE : I have deleted the first line in the dataset as it was unnecessary
# Function to load graph
def LoadGraph():
    with open("ClusteringDataSet.txt") as file:
        lines = file.readlines()
        graph = [(int(line.split()[0]), int(line.split()[1]), int(line.split()[2])) for line in lines]
    return graph

def Cluster (graph , k):
    # Intialising nodes
    nodes = set()
    for node , neighbour ,distance in graph:
        nodes.add(node)
        nodes.add(neighbour)
    # Creating clusters
    group = UnionFind(nodes)
    # Sorting graph based on distance 
    graph.sort(key = lambda x: x[2])
    totalClusters = len(nodes)
    # Main clustering loop
    for node , neighbour , distance in graph:
        if group.Find(node) != group.Find(neighbour):
            if totalClusters == k: # Break if no. of totalClusters is equal to k
                break
            group.Union(node ,neighbour)
            totalClusters -= 1
    # Returning minimum distance (or maximum spacing)
    for node , neighbour ,distance in graph:
        if group.Find(node) != group.Find(neighbour):
            return distance

# Computing answers
graph = LoadGraph()
print(Cluster(graph , 4))

# Ans = 106