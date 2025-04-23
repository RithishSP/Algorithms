import collections
import time

# Function to get data into 1D arr
def LoadArray():
    with open('2SumDataSet.txt') as file: 
        arr = [int(line.strip()) for line in file]
    return arr 

def TwoSumForAll(arr):
    # Initialising 
    startTime = time.time()
    seen = set(arr)
    possible = set()
    freq = collections.defaultdict(int) # 
    for n in arr:
        freq[n] += 1
    print("Running TwoSum...")
    # Double loop through all possible values of distinct n and through all sums
    for n in freq:
        for sum in range(-10000,10000+1):
            if sum - n in seen and (sum - n != n or freq[n]>=2):
                possible.add(sum) # Using set name sum to avoid duplicate entries of same sum 
                print(len(possible)) # Printing current length to show that loop is running
    # Calculating and displaying time
    totalTime=time.time()-startTime
    minutes = int(totalTime//60)
    seconds = totalTime%60
    print(f"Execution time: {minutes} mins and {seconds:.4f} secs")
    # Returning set of possible sums
    return possible

# Computing Answers
array = LoadArray()
possible = TwoSumForAll(array)
print(f"The answer is: {len(possible)}")

# Ans = 427 
# Running time takes around 45 mins 