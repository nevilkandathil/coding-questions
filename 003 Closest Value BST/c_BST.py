def findClosestValueInBst(tree, target):
	return closestValue(tree, target, tree.value)
'''
Method 1
Average: time O(log(n))| space O(1)
Worst: time O(n) | space O(1)
'''

# Using recursion		
def closestValue(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if currentNode.value > target:
            currentNode = currentNode.left
        elif currentNode.value < target:
            currentNode = currentNode.right
        else:
            break
    return closest
		
'''
Method 2
Average: time O(log(n))| space O(log(n))
Worst: time O(n) | space O(n)
'''

# def closestValue(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     if target < tree.value:
#         return closestValue(tree.left , target, closest)
#     elif target > tree.value:
#         return closestValue(tree.right, target, closest)
#     else: 
#         return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


'''
Test by creating any required binary tree
'''