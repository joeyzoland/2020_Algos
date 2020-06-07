# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        #Record the root value, and iterate through the tree
        #If you get through the entire tree, return True
        #Else, return False
        value = root.val
        valid = True
        def recursiveUnival(node):
            nonlocal valid
            if node == None:
                return
            elif valid:
                if node.val != value:
                    valid = False
                    return
            recursiveUnival(node.left)
            recursiveUnival(node.right)
        recursiveUnival(root)
        return valid

root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(2)
solution = Solution()
print(solution.isUnivalTree(root))
