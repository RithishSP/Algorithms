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

# Lomuto Partition
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
    global comparisons

    for j in range(left, right + 1):
        if arr[j] < arr[start]:
            arr[left], arr[j] = arr[j], arr[left]   # Main Partition step
            left += 1
    arr[left - 1], arr[start] = arr[start], arr[left - 1]   # Swapping pivot back to its spot to finish partition
    comparisons += right - start
    return left - 1

def QuickSort(arr , start, end , mode):
   if start < end:
      p = Partition(arr , start , end , mode)
      QuickSort(arr , p+1 , end , mode)
      QuickSort(arr , start , p-1 , mode)
      # Recursive QuickSort

comparisons = 0
QuickSort(arr , start , end , 'first')
print(comparisons)

'''
Pivots,
    First = 162085
    Last = 164123
    Median of Three = 138382
'''
    
    
