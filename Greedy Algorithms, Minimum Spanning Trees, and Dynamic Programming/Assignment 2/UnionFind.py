class UnionFind:
    def __init__(self, elements):
        self.parent = {element: element for element in elements} # Defining parent for each element
    
    def Find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.Find(self.parent[i]) # Recursive call to find parent
        return self.parent[i] # Base case

    def Union(self, i, j):
        iRoot = self.Find(i) # Finding parent of i
        jRoot = self.Find(j) # Finding parent of j
        if iRoot != jRoot: 
            self.parent[iRoot] = jRoot # Points the root of i to root of j : combining them