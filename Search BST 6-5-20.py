"""
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2
     / \
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        #At each node, check if the node's value = the one under search
            #If it does match, return the node
        #Run the function on each of the children
            #If at any point the function does not return None, return the node
            #Otherwise, return None
        if root == None:
            return None
        if root.val == val:
            return root
        left_result = self.searchBST(root.left, val)
        if left_result != None:
            return left_result
        right_result = self.searchBST(root.right, val)
        if right_result != None:
            return right_result
        return None

solution = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

output_node = solution.searchBST(root, 2)
print(output_node.val, output_node.left.val, output_node.right.val)
