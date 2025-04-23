# NOTE : I have deleted the first line in the dataset as it was unnecessary
# Function to get data into list of tuples
def LoadData():
    jobs = []
    with open('JobSchedulingDataSet.txt') as file: 
        for line in file:
            parts = line.strip().split()
            jobs.append(tuple(int(job) for job in parts))
    return jobs

def DifferenceScheduling (jobs):
    # Sorting based on difference breaking ties with greater weight
    sortedJobs = sorted(jobs, key = lambda job: (job[0] - job[1], job[0]), reverse=True)
    completionTime , time = 0 , 0
    # Computing and returning weighted completion times
    for weight, length in sortedJobs:
        time += length
        completionTime += weight*time
    return completionTime

def RatioScheduling (jobs):
    # Sorting based on ratio keeping ties in original order
    sortedJobs = sorted(jobs, key = lambda job: (job[0] / job[1]), reverse = True)
    completionTime , time = 0 , 0
    # Computing and returning weighted completion times
    for weight, length in sortedJobs:
        time += length
        completionTime += weight*time
    return completionTime

# Computing answers
jobs = LoadData()
print(DifferenceScheduling(jobs))
print(RatioScheduling(jobs))

'''
Difference Scheduling = 69119377652
Ratio Scheduling = 67311454237
'''