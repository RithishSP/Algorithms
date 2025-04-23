from itertools import combinations
from math import sqrt, inf
from time import time

# Function to load arrays
def LoadArrays():
    cities = []
    with open('TSPDataSet.txt') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        for line in lines[1:]:
            parts = line.strip().split()
            cities.append((float(parts[0]), float(parts[1])))
    return n, cities

# Precompute distances of all combinations and store it in a matrix
def ComputeDistances(n, cities):
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distances[i][j] = sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return distances

# Main TSP function
def TSP(n, cities):
    startTime = time()
    # Storing distances of all city combinations
    distances = ComputeDistances(n, cities)
    # Intialising solutions dictionary with base case
    solution = {}
    solution[((0,), 0)] = 0
    # Outer 2 for loops iterate through subsets which have atleast 2 elements 
    for m in range(2, n+1): # m is the subproblem size
        newSolution = {}  # Only store results for current m-sized subsets
        for subSet in combinations(range(n), m): 
            if 0 not in subSet: # Skip subsets which dont include starting city
                continue
            for j in subSet: 
                if j == 0: # Skip if j is starting city
                    continue
                # Form previous subset by removing j
                prevSubSet = tuple(k for k in subSet if k != j)
                minCost = inf
                # Loop through all previous cities k that lead to j
                for k in prevSubSet: 
                    if (prevSubSet, k) in solution:
                        prevCost = solution[(prevSubSet, k)] + distances[k][j]
                        if prevCost < minCost:
                            minCost = prevCost
                # Store the minimum cost found
                newSolution[(subSet, j)] = minCost
        solution = newSolution  # Discard previous smaller subsets to save memory
    # Now compute minimum cost of returning to starting city
    allCities = tuple(range(n))
    minPathCost = inf
    for j in range(1, n): # Try ending at every city j 
        if (allCities, j) in solution:
            pathCost = solution[(allCities, j)] + distances[j][0] # Return to start if it exists
            if pathCost < minPathCost:
                minPathCost = pathCost
    # Compute and display running time
    totalTime = time() - startTime
    minutes = int(totalTime // 60)
    seconds = totalTime % 60
    print(f"Execution time: {minutes} mins and {seconds:.2f} secs")
    # Return mincost of path taken
    return minPathCost

# Computing answer
n, cities = LoadArrays()
print(int(TSP(n, cities)))

# Ans = 26442
# Execution time is about 50 mins 

# Note to self ; check this link later for optimisation,
# https://www.coursera.org/learn/algorithms-npcomplete/discussions/forums/MdMEsnblEeaa3A5N6H7-Uw/threads/eMOekvYIEeyhlwpGw76VXQ