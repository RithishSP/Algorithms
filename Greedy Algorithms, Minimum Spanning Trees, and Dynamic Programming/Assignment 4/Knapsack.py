import time

# NOTE : I have deleted the first line in both datasets as it was unnecessary
# Function to load the arrays based on what file to use as the data set
def LoadArrays(mode):
    if mode.lower() == 's':
        capacity = 10000
        values , weights = [] , []
        with open('KnapsackDataSet.txt') as file:
            for line in file:
                parts = line.strip().split()
                values.append(int(parts[0]))
                weights.append(int(parts[1]))
        return capacity, values, weights
    else:
        capacity = 2000000
        values , weights = [] , []
        with open('KnapsackBigDataSet.txt') as file:
            for line in file:
                parts = line.strip().split()
                values.append(int(parts[0]))
                weights.append(int(parts[1]))
        return capacity, values, weights

def Knapsack(capacity , values , weights):
    startTime = time.time()
    # Initialising solutions for iterative DP
    solutions=[0 for _ in range(capacity+1)]
    # Main DP loop
    for i in range(len(values)): 
        # Iterating backwards to not use same value twice
        for j in range(capacity, weights[i] - 1, -1): 
            # If including current value increases weight of solution, add it
            solutions[j] = max(solutions[j] , solutions[j - weights[i]] + values[i])
    # Calculating and printing time taken to run the function
    totalTime = time.time() - startTime
    minutes = int(totalTime//60)
    seconds = totalTime%60
    print(f"Execution time: {minutes} mins and {seconds:.2f} secs")
    return solutions[capacity]
    
# Computing answer
capacity , values , weights = LoadArrays('s')
print(Knapsack(capacity , values, weights))

'''
Small = 2493893
Big = 4243395
Execution time for big data set is around 10 mins
'''