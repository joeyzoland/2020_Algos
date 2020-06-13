"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.



Example 1:

Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".


Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.
"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        #Search through the string
            #If you find a duplicate, remove and repeat
        counter = 0
        output = S
        while counter + 1 < len(output):
            if output[counter] == output[counter + 1]:
                output = output[:counter] + output[counter + 2:]
                if counter != 0:
                    counter -= 1
            else:
                counter += 1
        return output

solution = Solution()
input = "abbaca"
print(solution.removeDuplicates(input))
