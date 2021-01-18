'''
Method 1
O(n) time | O(d) space - where n is the total number of elemnts in the array,
including sub-elements, and d is the greatest depth of "special" arrays in the array
'''
def productSum(array, depth=1):
    # Write your code here.
	aSum = 0
	for ele in array:
		if type(ele) is list:
			return productSum(ele, depth+1)
		else:
			aSum += ele
	return aSum * depth