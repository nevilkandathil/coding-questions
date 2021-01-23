'''
Method 1
O(n) time | O(h) space - where n in the number of nodes
in the binary tree and h is the heigh tof the Binary Tree
'''

def nodeDepths(root):
    # Write your code here.
    stack = [{"node": root, "depth":0}]
    sumOfDepths = 0
    while len(stack) > 0:
        currentNode = stack.pop()
        node, depth = currentNode["node"], currentNode["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth+1})
        stack.append({"node": node.right, "depth": depth+1})
    return sumOfDepths

'''
Method 2
'''
# def nodeDepths(root, depth=0):
#     # Write your code here.
#     if root is None:
#         return 0
#     return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None