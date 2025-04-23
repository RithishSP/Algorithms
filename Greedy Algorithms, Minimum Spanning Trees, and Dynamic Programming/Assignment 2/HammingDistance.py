from UnionFind import UnionFind
from collections import defaultdict
from itertools import combinations

# NOTE : I have deleted the first line in the dataset as it was unnecessary
# Function to load graph
def LoadGraph():
    nodes = defaultdict(list)
    i = 0
    with open ("HammingDistanceDataSet.txt") as file:
        for line in file:
            x =''.join(line.split())
            nodes[int(x , 2)].append(i)
            i+=1
    return nodes

# Function to get all 1 bit flipped versions of a binary number n
def HammingDistance1(n):
    # Initialising
    bitLength = n.bit_length()
    output = []
    # Flipping 1 bit each time and append it to output
    for i in range(bitLength):
        flipped = n ^ (1 << i) 
        output.append(flipped)
    return output

# Function to get all 2 bit flipped versions of a binary number n
def HammingDistance2(n):
    # Initialising 
    bitLength = n.bit_length()
    output = []
    # Flipping each combination of 2 bits and append it to output
    for i, j in combinations(range(bitLength), 2):
        flipped = n ^ (1 << i) 
        flipped ^= (1 << j)
        output.append(flipped)
    return output

# Main function to calculate number of clusters
def Cluster(nodes):
    # Initialising
    totalClusters = UnionFind(nodes)
    # Adding all nodes of hamming distance 1 to a cluster
    for n in nodes:
        for code in HammingDistance1(n):
            if code in nodes:
                totalClusters.Union(n,code)
    # Adding all nodes of hamming distance 2 to a cluster
    for n in nodes:
        for code in HammingDistance2(n):
            if code in nodes:
                totalClusters.Union(n,code)
    # Returning the number of clusters
    return len(set(totalClusters.Find(x) for x in nodes))

# Computing Answer
graph = LoadGraph()
print(Cluster(graph))

# Ans = 6118