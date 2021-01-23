# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

'''
O(n) time | O(n) space - n is the number of nodes
'''

def branchSums(root):
    # Write your code here.
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, currentSum, sums):
    if node is None:
        return
    
    newSum = currentSum + node.value
    if node.left is None and node.right is None:
        sums.append(newSum)
        return

    calculateBranchSums(node.left, newSum, sums)
    calculateBranchSums(node.right, newSum, sums)
