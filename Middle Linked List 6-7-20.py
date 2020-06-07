"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.



Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import math
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #Iterate through the list to find the length
        #Iterate through the list one more time to find the correct node, flooring len / 2
        length = 0
        current = head
        while current is not None:
            current = current.next
            length += 1
        steps = math.floor(length / 2)
        current = head
        while steps > 0:
            current = current.next
            steps -= 1
        return current

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
solution = Solution()
print(solution.middleNode(root).val)
