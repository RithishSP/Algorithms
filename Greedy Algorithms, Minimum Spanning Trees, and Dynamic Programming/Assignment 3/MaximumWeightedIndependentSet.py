# NOTE : I have deleted the first line in the dataset as it was unnecessary
# Function to load Array
def LoadArray():
    with open ("MaximumWeightedIndependentSetDataSet.txt") as file:
        weights = [int(line.strip()) for line in file]
    return weights

def MWIS(weights):
    # Initialising solutions
    solution = [0]*(len(weights) + 1)
    solution[1] = weights[0]
    # DP to compute the solution for each length of the input weights
    for i in range(2 , len(weights)+1):
        solution[i] = max(solution[i-1], solution[i-2]+ weights[i-1])
    # Initialising solution set to contain nodes used in solution
    solutionSet = []
    i = len(weights)
    # Looping through all indices of solutions
    while i >= 1:
        # Check if solution had included node i
        if solution[i] > solution[i-2] + weights[i-1]:
            i-=1
        # Else add node i 
        else:
            solutionSet.append(i)
            i-=2
    # Reversing and returning solution set in order of ascending nodes
    solutionSet.reverse()
    return solutionSet

# Computing answer
nodeWeights = LoadArray()
solutionSet = MWIS(nodeWeights)
toCheck = [1, 2, 3, 4, 17, 117, 517, 997]
answerArray = ['1' if node in solutionSet else '0' for node in toCheck]
print(''.join(answerArray))

# Ans = 10100110

