def binarySearch(array, target):    
	return binarySearchHelper(array, target, 0, len(array)-1)
'''
Method 1
O(log(n)) time | O(1) space
'''
def binarySearchHelper(array, target, left, right):
	while left <= right:
		mid = (left+right)//2
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	return -1

'''
Method 2
O(log(n)) time | O(log(n)) space
'''
# def binarySearchHelper(array, target, left, right):
#     if left > right:
#         return -1
#     mid = (left+right)//2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         binarySearchHelper(array, target, left, mid-1)
#     else:
#         binarySearchHelper(array, target, mid+1, right)