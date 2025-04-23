import heapq

# Function to get data into a 1D array
def LoadArray():
    with open('HeapSortDataSet.txt') as file: # Same data set as QuickSort, just renamed
        arr = [int(line.strip()) for line in file]
    return arr

# Initialising two arrays for two different ways of Heap Sort
arr1 = LoadArray()
arr2 = LoadArray()

# Function to check if elements are sorted
def IsSorted(arr):
    return all(arr[i]<=arr[i+1] for i in range(0, len(arr)-1))

# Sorting using heapq defined functions
def HeapSortUsingHeapq(arr):
    heapq.heapify(arr) # Heapify array with min element at root
    sortedarr = []
    while arr:
        sortedarr.append(heapq.heappop(arr)) # Pop min element and append to sorted array
    return sortedarr

# Defining Heapify function with max element at root
def MaxHeapify(arr , size , rootIndex):
    # Initialising root index, left and right childs
    largest = rootIndex
    leftChild =  2*rootIndex + 1
    rightChild = 2*rootIndex + 2
    # Update largest if left or right child exists and is larger than root index
    if leftChild < size and arr[leftChild] > arr[largest]:
        largest = leftChild
    if rightChild < size and arr[rightChild] > arr[largest]:
        largest = rightChild
    if largest != rootIndex:
        arr[largest] , arr[rootIndex] = arr[rootIndex] , arr[largest]
        MaxHeapify(arr , size , largest) # Make sure every subtree is a heap

# Sorting using user defined function with less memory complexity
def HeapSortWithoutHeapq(arr):
    size = len(arr)
    for i in range(size//2, -1 , -1): # Building heap from last leaf up to the main root
        MaxHeapify(arr,size,i)
    for i in range(size-1, 0 , -1): # Sorting by keeping the largest element at the end in same array
        arr[i] , arr[0] = arr[0] , arr[i]
        MaxHeapify(arr,i,0) # Reducing size of heap as array gets sorted 

# Printing outputs
print(IsSorted(HeapSortUsingHeapq(arr1)))
HeapSortWithoutHeapq(arr2)
print(IsSorted((arr2)))