'''
O(nlog(n)) time | O(1) space - where n is the number of queries
'''

def minimumWaitingTime(queries):
    minTime = 0
    queries.sort()
    for idx, num in enumerate(queries):
        minTime += (len(queries)-(idx+1)) * num
    return minTime

if __name__ =="__main__":
    print(minimumWaitingTime([3,2,1,2,6]))