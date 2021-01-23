# uncomment required methods
def twoNumberSum(array, targetSum):
    
    '''
    Method 1
    
    Time: O(n)
    Space: O(n)
    '''
    # result = []
    # checked = {}
    
    # for x in array:
    # 	y = targetSum - x
    # 	if y in list(checked.keys()):
    # 		result.extend((x,y))
    # 	checked[x] = True
    # return result


    '''
    Method 2
    
    Time: O(nlog(n))
    Space: O(1)
    '''
    result = []
    array = sorted(array)
    low = 0
    high = len(array) - 1

    while low < high:
    	tempSum = array[low] + array[high]
	if tempSum > targetSum:
    		high -= 1
    	elif tempSum < targetSum:
    		low += 1
    	else:
    		result.extend((array[low], array[high]))
    		return result


def main():
    x = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
    print(x)

main()