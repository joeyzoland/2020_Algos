"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""

class Solution:
    def peakIndexInMountainArray(self, A):
        #Record current index and past height
        #Iterate through heights until we see a decline, in which case we return the last index
        #If we haven't found the peak, update current index and past height
        current_index = 1
        past_height = A[0]
        while True:
            if past_height > A[current_index]:
                return current_index - 1
            past_height = A[current_index]
            current_index += 1

Solution = Solution()
print(Solution.peakIndexInMountainArray([0,2,1,0]))
