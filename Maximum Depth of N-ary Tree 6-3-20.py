# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        #If what you're looking at is None, return 0
        #Establish a variable representing the maximum leaves from the node, starting at 0
        #Iterate through all of that node's children
            #If the node you're on exceeds the max leaves, update the variable
        #Return 1 + the max leaves variable
        if root == None:
            return 0
        max_leaves = 0
        for child in root.children:
            max_leaves = max(max_leaves, self.maxDepth(child))
        return 1 + max_leaves

#Test Case
#           1
#       /   |   \
#      3    2   4
#     / \
#    5  6

first_tree_node = Node(1)
node3 = Node(3)
node3.children = [Node(5), Node(6)]
first_tree_node.children = [node3, Node(2), Node(4)]
Solution = Solution()

print(Solution.maxDepth(first_tree_node))
