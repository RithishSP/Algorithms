from heapq import heappop , heappush

# Function to get data into 1D arr
def LoadArray():
    with open('MedianMaintenanceDataSet.txt') as file: 
        arr = [int(line.strip()) for line in file]
    return arr

def MedianMaintenance(arr):
    # Initialising
    medians = []
    lowHeap = []
    highHeap = []
    # Looping for every element added
    for num in arr: 
        # Adding element depending on where it belongs
        if len(lowHeap)==0 or num <= -lowHeap[0]: 
            heappush(lowHeap,-num)
        else:
            heappush(highHeap,num)
        # Balancing the heaps and keeping median at lowHeap
        if len(lowHeap) - len(highHeap) > 1: 
            heappush(highHeap,-heappop(lowHeap))
        elif len(highHeap)>len(lowHeap):
            heappush(lowHeap,-heappop(highHeap))
        # Adding median of this iteration to medians
        medians.append(-lowHeap[0]) 
    return medians

# Printing answer
array = LoadArray()
print(sum(MedianMaintenance(array))%10000)

# Ans = 1213











