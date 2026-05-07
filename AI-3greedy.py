class Job: 
    def __init__(self, id, deadline, profit): 
        self.id = id 
        self.deadline = deadline 
        self.profit = profit 
 
def job_scheduling(jobs): 
    # Sort jobs by profit (Greedy) 
    jobs.sort(key=lambda x: x.profit, reverse=True) 
 
    # Find max deadline 
    max_deadline = max(job.deadline for job in jobs) 
 
    # Create slots 
    slots = ['-'] * max_deadline 
    total_profit = 0 
 
    # Assign jobs 
    for job in jobs: 
        for i in range(job.deadline - 1, -1, -1): 
            if slots[i] == '-': 
                slots[i] = job.id 
                total_profit += job.profit 
                break 
 
    return slots, total_profit 
 
# Input 
jobs = [ 
    Job("j1", 2, 15), 
    Job("j2", 3, 27), 
    Job("j3", 3, 10), 
    Job("j4", 3, 100), 
    Job("j5", 4, 150) 
] 
 
# Call function 
result, profit = job_scheduling(jobs) 
 
# Output 
print("Scheduled Jobs:", result) 
print("Total Profit:", profit) 
