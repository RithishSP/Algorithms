from heapq import heappush,heappop,heapify

# NOTE : I have deleted the first line in the dataset as it was unnecessary
# Function to load Array
def LoadArray():
    with open ("HuffmanCodingDataSet.txt") as file:
        letters = [int(line.strip()) for line in file]
    return letters

# Main function to get only max depth and not the actual codes
def HuffmanCodingDepth(letters):
    # Making heap of code weights and depths
    codes = [(weight , 0 , 0) for weight in letters]
    heapify(codes)
    # Loop to merge minimum weights until one element remains
    while len(codes)>1:
        weight1 , min1, max1 = heappop(codes)
        weight2 , min2, max2 = heappop(codes)
        # +1 depth as node has been added above after merging
        newMinLength = 1 + min(min1 , min2)
        newMaxLength = 1 + max(max1 , max2)
        # Adding merged codes back in heap
        heappush(codes , (weight1 + weight2, newMinLength , newMaxLength))
    # Returning Final Min and Max Length
    return codes[0][1] , codes[0][2]

# Computing answers
letters = LoadArray()
print(HuffmanCodingDepth(letters))

'''
Minimum code length = 9
Maximum code length = 19
'''