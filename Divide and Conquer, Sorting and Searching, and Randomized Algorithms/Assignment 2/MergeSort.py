with open('MergeSortDataSet.txt') as file:
    array = [int(line.strip()) for line in file]

def Same(array): # Check if all elements are same to remove redundant steps
    for i in range (1,len(array)):
        if array[i-1] != array[i]:
            return 0
    return 1

def MergeSort(array):

    if Same(array): # Not needed in this case as all elements are unique but general optimization
        return array , 0
    
    n = len(array)
    i , j  = 0 , 0 
    output = []
    part1 , count1 = MergeSort(array[:(n//2)])  # Recursively sorting each half 
    part2 , count2 = MergeSort(array[(n//2):])
    count = count1 + count2
    while i < len(part1) and j < len(part2): # Appending elements based on if its bigger or not  
        if part1[i] <= part2[j]:
            output.append(part1[i])    
            i += 1
        else:
            count += len(part1) - i # Count increased as it is an inversion
            output.append(part2[j]) 
            j +=1
    if i < len(part1): 
        output += part1[i:] # Rest of elements added to the rest of the output
    if j < len(part2):
        output += part2[j:]
    
    return output , count
    
print(MergeSort(array)[1])

#Ans = 2407905288