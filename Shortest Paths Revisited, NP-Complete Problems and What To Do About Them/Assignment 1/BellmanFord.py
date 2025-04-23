from math import inf    
from time import time

# Function to load graph
def LoadGraph(filename):
    graph = []
    with open(filename) as file:
        lines = file.readlines()
        n, m = int(lines[0].split()[0]), int(lines[0].split()[1])
        for line in lines[1:]:
            v1, v2, w = map(int, line.split())
            graph.append((v1-1, v2-1, w)) # v1-1 and v2-1 to make vertices start from 0 instead of 1
    return graph, n # n is the number of nodes

def BellmanFord(graph, n, source):
    # Initialising distances of all nodes from source
    distances = [inf] * n
    distances[source] = 0
    # Main DP loop
    for i in range(n):
        #Re-initialising updated for each instance of the no. of nodes used
        updated = False
        for v1, v2, weight in graph:
            # If distance of v1 + weight between v1 and v2 is less than distance of v2, update it
            if distances[v1] != inf and distances[v1] + weight < distances[v2]:
                updated = True
                if i == n - 1:
                    # If number of nodes used is n-1 then there is a negative cycle, so return None
                    return None 
                else:
                    # Else update new distance of v2
                    distances[v2] = distances[v1] + weight
        # If distance was not updated in this iteration, then it wont be in the next, so break
        if not updated:
            break
    return distances

# Function to invoke BellmanFord n times
def APSP(graph, n):
    startTime = time()
    minDistances = []
    for source in range(n):
        distances = BellmanFord(graph, n, source)
        if distances is None:
            # If there was a negative cycle
            return 'NULL'
        else:
            # Else append minimum of the distances
            minDistances.append(min(distances))
    # Compute and display execution time
    totalTime = time() - startTime
    minutes = int(totalTime // 60)
    seconds = totalTime % 60
    print(f"Execution time: {minutes} mins and {seconds:.2f} secs")
    # return minimum of the mininimum distances
    return min(minDistances)

# Computing answers
graph, n = LoadGraph('APSPDataSet1.txt')
print(APSP(graph, n))
graph , n = LoadGraph('APSPDataSet2.txt')
print(APSP(graph , n))
graph , n = LoadGraph('APSPDataSet3.txt')
print(APSP(graph ,n))

'''
APSPDataSet1 = NULL
APSPDataSet2 = NULL
APSPDataSet3 = -19
So, Ans = -19
Note: Running time for all three data sets is around 2 mins in total
'''