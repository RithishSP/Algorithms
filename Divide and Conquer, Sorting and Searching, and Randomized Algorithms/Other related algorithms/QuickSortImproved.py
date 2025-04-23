with open('QuickSortDataSet.txt') as file:
    arr = [int(line.strip()) for line in file]

start = 0
end = len(arr)-1
global comparisons

# Median of three is by far the best reducing chances of getting high or low values
def Median_of_three(array, first, middle, last):
    if min(array[first], array[last]) < array[middle] < max(array[first], array[last]):
        return middle
    elif min(array[middle], array[last]) < array[first] < max(array[middle], array[last]):
        return first
    else:
        return last

# Hoare's Partition
def Partition(arr,start,end,mode):
    if mode == 'first':
       pivot = start
    elif mode == 'last':
       pivot = end
    else:
       pivot = Median_of_three(arr, start, start + (end - start) // 2, end)

    arr[pivot] , arr[start] = arr[start] , arr[pivot]  # Placing pivot in starting position
    left = start+1
    right = end
    pivot = start # Making index of pivot correct again
    global comparisons

    while True:
        while left <= right and arr[left]<arr[pivot]: 
            left+=1
        while left <= right and arr[right]>arr[pivot]:
            right-=1
        if left<=right:
            arr[left] , arr[right] = arr[right] , arr[left]     
        else:
            break

    arr[right], arr[start] = arr[start], arr[right]   # Swapping pivot back to its spot to finish partition
    comparisons+= end - start # Hoare's Partition does more comparisons but less swaps making it more efficient
    return right

def QuickSort(arr , start, end , mode):
   if start < end:
      p = Partition(arr , start , end , mode)
      QuickSort(arr , p+1 , end , mode)
      QuickSort(arr , start , p-1 , mode)
      # Recursive QuickSort

comparisons = 0
QuickSort(arr , start , end , '')
print(comparisons)
    
