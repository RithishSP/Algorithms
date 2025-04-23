from time import time
from math import sqrt

# Function to load arrays
def LoadArrays():
    cities = []
    with open('NearestNeighbourTSPDataSet.txt') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        for line in lines[1:]:
            parts = line.split()
            cities.append((float(parts[1]), float(parts[2])))
    return n, cities


def Distance(cities , i , j):
    return sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

def NNTSP(n ,cities):
    startTime = time()
    # Intialising distance and visited array
    distance = 0.0
    visited = [0]
    # Main for loop to go through all cities except start one by one
    for _ in range(n - 1):
        # Getting last visited city
        lastVisited = visited[-1]
        # Unvisited is the total cities - cities that have been visited
        unvisited = set(range(n)) - set(visited)
        # Computing distance for all other cities and getting min distance and next city
        minDistance , nextCity= min([(Distance(cities, lastVisited, city) , city) for city in unvisited])
        distance += minDistance
        visited.append(nextCity)
        print(_) # Printing iteration while it runs
    # Compute and display running time
    totalTime = time() - startTime
    minutes = int(totalTime // 60)
    seconds = totalTime % 60
    print(f"Execution time: {minutes} mins and {seconds:.2f} secs")
    # Returning distance + distance to reach start city
    return int(distance + Distance(cities, visited[-1], visited[0]))

# Computing Answers
n , cities = LoadArrays()
if len(cities) == n:
    print(NNTSP(n, cities))
else:
    print("Not equal")

# Ans = 1203406
# Execution time is around 13 mins  